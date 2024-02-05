import unittest
from transaction_builder_script import generate_redeeem_script, get_address_from_script, create_transaction, create_child_transaction

class TestYourScript(unittest.TestCase):

    def test_generate_redeem_script(self):
        preimage_hex = '427472757374204275696c64657273'
        redeem_script = generate_redeeem_script(preimage_hex)
        # Assert that the returned redeem script is as expected
        # You might need to adjust this depending on the actual implementation of your function
        self.assertEqual(redeem_script, expected_result)

    def test_get_address_from_script(self):
        redeem_script = ... #sample redeem script here
        address = get_address_from_script(redeem_script)
        # Assert that the returned address is as expected
        # Again, adjust this depending on your function's actual implementation
        self.assertEqual(address, expected_result)

    def test_create_transaction(self):
        private_key = ... #sample private key here
        source_address = ... #sample source address here
        destination_address = ... #sample destination address here
        transaction = create_transaction(private_key, source_address, destination_address)
        # Assert that the returned transaction is as expected
        # Adjust this depending on your function's actual implementation
        self.assertEqual(transaction, expected_result)

    def test_create_child_transaction(self):
        parent_txid = ... #sample parent transaction ID here
        parent_vout = ... #sample parent vout here
        parent_scriptPubKey = ... #sample parent scriptPubKey here
        parent_redeemScript = ... #sample parent redeemScript here
        private_key = ... #sample private key here
        destination_address = ... #sample destination address here
        change_address = ... #sample change address here
        send_amount = ... #sample send amount here
        child_transaction = create_child_transaction(parent_txid, parent_vout, parent_scriptPubKey, parent_redeemScript, private_key, destination_address, change_address, send_amount)
        # Assert that the returned child transaction is as expected
        # Adjust this depending on your function's actual implementation
        self.assertEqual(child_transaction, expected_result)

if __name__ == "__main__":
    unittest.main()
