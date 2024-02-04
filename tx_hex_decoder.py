# store the transaction as bytes 
raw_tx = bytes.fromhex('0100000001c997a5e56e104102fa209c6a852dd90660a20b2d9c352423edce25857fcd3704000000004847304402204e45e16932b8af514961a1d3a1a25fdf3f4f7732e9d624c6c61548ab5fb8cd410220181522ec8eca07de4860a4acdd12909d831cc56cbbac4622082221a8768d1d0901ffffffff0200ca9a3b00000000434104ae1a62fe09c5f51b13905f07f06b99a2f7159b2225f374cd378d71302fa28414e7aab37397f554a7df5f142c21c1b7303b8a0626f1baded5c72a704f7e6cd84cac00286bee0000000043410411db93e1dcdb8a016b49840f8c53bc1eb68a382e97b1482ecad7b148a6909a5cb2e0eaddfb84ccf9744464f82e160bfa9b8b64f9d4c03f999b8643f656b412a3ac00000000')

# import hashlib for sha256
import hashlib

# first round of sha256
hash1 = hashlib.sha256(raw_tx).digest()

# second round of sha256 gives us the txid
hash2 = hashlib.sha256(hash1).digest()

print("Two rounds of SHA256 on the raw tx gives us: ", hash2.hex())

# We can use the python shorthand '[::-1]' to reverse the bytes, giving us the output in little endian notation
txid = hash2[::-1]
print("Reversing the bytes to little endian: ", txid.hex())

# Transaction size
size = len(raw_tx)
print("size: ", size)

# Transaction weight
weight = size*4
print("weight: ", weight)

# Virtual size
import math
vsize = math.ceil(weight/4) # Note that vsize/vbytes will round up
print("vsize: ", vsize)

# Version
version = raw_tx[0:4][::-1].hex()
print("version: ", int(version, 16))

# Number of inputs
num_inputs = raw_tx[4]
print("num_inputs: ", num_inputs)

# Inputs
inputs = []
for i in range(num_inputs):
    offset = 5 + i*41
    input = raw_tx[offset:offset+41]
    inputs.append(input.hex())
print("inputs: ", inputs)

# Number of outputs
num_outputs_offset = 5 + num_inputs*41
num_outputs = raw_tx[num_outputs_offset]
print("num_outputs: ", num_outputs)

# Outputs
outputs = []
for i in range(num_outputs):
    offset = num_outputs_offset + 1 + i*33
    output = raw_tx[offset:offset+33]
    outputs.append(output.hex())
print("outputs: ", outputs)

# Locktime
locktime = raw_tx[-4:][::-1].hex()
print("locktime: ", int(locktime, 16))
