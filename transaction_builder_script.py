from bitcoin import SelectParams
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret, P2PKHBitcoinAddress
from bitcoin.core import b2lx, lx, COIN, COutPoint, CMutableTxOut, CMutableTxIn, CMutableTransaction
from bitcoin.core.script import CScript, OP_SHA256, OP_EQUAL, OP_DUP, OP_HASH160, OP_EQUALVERIFY, OP_CHECKSIG
from bitcoin.core.scripteval import VerifyScript, SCRIPT_VERIFY_P2SH
from bitcoin.core.script import SignatureHash, SIGHASH_ALL




preimage_hex = '427472757374204275696c64657273'

def generate_redeeem_script(preimage_hex):


    # Create the redeem script
    redeem_script = CScript([OP_SHA256, bytes.fromhex(preimage_hex), OP_EQUAL])

    print("redeem Script : ", redeem_script)
    return redeem_script


def get_address_from_script(redeem_script):

    # Get the scriptPubKey of the P2SH address
    scriptPubKey = redeem_script.to_p2sh_scriptPubKey()

    # Convert the scriptPubKey to an address
    p2sh_address = CBitcoinAddress.from_scriptPubKey(scriptPubKey)

    print('address', p2sh_address)
    return p2sh_address

def create_transaction(private_key, source_address, destination_address):
    # network  set to testnet
    SelectParams('testnet')

    # Replace these with your actual private key and addresses
    private_key = CBitcoinSecret(private_key)
    source_address = CBitcoinAddress(source_address)
    destination_address = CBitcoinAddress(destination_address)

    # This is the transaction id (txid) and index of the UTXO you want to spend
    txid = lx('UTXO_txid')
    vout = 0

    # This is the amount of Bitcoins in the UTXO you want to spend
    amount = 1*COIN

    # This is the amount of Bitcoins you want to send
    send_amount = int('amount_to_send'*COIN)

    # This is the transaction fee you want to pay (0.001 BTC)
    fee = int(0.001*COIN)

    # Calculate the change amount
    change_amount = amount - send_amount - fee

    # Create a mutable transaction
    tx = CMutableTransaction()

    # Add the input (the UTXO)
    txin = CMutableTxIn(COutPoint(txid, vout))
    tx.vin.append(txin)

    # Add the output (the destination address and the amount)
    txout = CMutableTxOut(send_amount, destination_address.to_scriptPubKey())
    tx.vout.append(txout)

    # Add the change output (back to the source address)
    if change_amount > 0:
        change_txout = CMutableTxOut(change_amount, source_address.to_scriptPubKey())
        tx.vout.append(change_txout)

    # Sign the transaction
    sighash = SignatureHash(source_address.to_scriptPubKey(), tx, 0, SIGHASH_ALL)
    sig = private_key.sign(sighash) + bytes([SIGHASH_ALL])
    txin.scriptSig = CScript([sig, private_key.pub])

    # Verify the signature
    VerifyScript(txin.scriptSig, source_address.to_scriptPubKey(), tx, 0, (SCRIPT_VERIFY_P2SH,))

    # Print the transaction in hexadecimal
    print(b2lx(tx.serialize()))


def create_child_transaction(parent_txid, parent_vout, parent_scriptPubKey, parent_redeemScript, private_key, destination_address, change_address, send_amount):
    # Create a mutable transaction
    tx = CMutableTransaction()

    # Add the input (the parent transaction output)
    txin = CMutableTxIn(COutPoint(lx(parent_txid), parent_vout))
    tx.vin.append(txin)

    # Add the output (the destination address and the amount)
    txout = CMutableTxOut(send_amount, CBitcoinAddress(destination_address).to_scriptPubKey())
    tx.vout.append(txout)

    # Calculate the change amount
    change_amount = parent_vout - send_amount - fee

    # Add the change output (to the change address)
    if change_amount > 0:
        change_txout = CMutableTxOut(change_amount, CBitcoinAddress(change_address).to_scriptPubKey())
        tx.vout.append(change_txout)

    # Sign the transaction
    sighash = SignatureHash(parent_scriptPubKey, tx, 0, SIGHASH_ALL)
    sig = private_key.sign(sighash) + bytes([SIGHASH_ALL])
    txin.scriptSig = CScript([sig, parent_redeemScript])

    # Verify the signature
    VerifyScript(txin.scriptSig, parent_scriptPubKey, tx, 0, (SCRIPT_VERIFY_P2SH,))

    # Print the transaction in hexadecimal
    print(b2lx(tx.serialize()))

