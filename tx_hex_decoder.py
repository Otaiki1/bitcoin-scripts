def decode_transaction(raw_tx):
     # Convert the raw transaction to bytes if it's not already
    if isinstance(raw_tx, str):
        raw_tx = bytes.fromhex(raw_tx)

    # Version
    version = raw_tx[0:4][::-1].hex()
    print("version: ", version)

    # Marker and flag (only present in SegWit transactions)
    marker = raw_tx[4]
    flag = raw_tx[5]
    print("marker: ", marker)
    print("flag: ", flag)

    # Number of inputs
    num_inputs = raw_tx[6]
    print("num_inputs: ", num_inputs)

    # Inputs
    inputs = []
    for i in range(num_inputs):
        offset = 7 + i*41
        input = raw_tx[offset:offset+41]
        inputs.append(input.hex())
    print("inputs: ", inputs)

    # Number of outputs
    num_outputs_offset = 7 + num_inputs*41
    num_outputs = raw_tx[num_outputs_offset]
    print("num_outputs: ", num_outputs)

    # Outputs
    outputs = []
    for i in range(num_outputs):
        offset = num_outputs_offset + 1 + i*33
        output = raw_tx[offset:offset+33]
        outputs.append(output.hex())
    print("outputs: ", outputs)

    # Witness data (only present in SegWit transactions)
    witness_offset = num_outputs_offset + 1 + num_outputs*33
    witness = raw_tx[witness_offset:-4]
    print("witness: ", witness.hex())

    # Locktime
    locktime = raw_tx[-4:][::-1].hex()
    print("locktime: ", locktime)
    
    return(version, num_inputs, inputs, num_outputs, outputs, locktime)


def test_decode_transaction():
    raw_tx = '020000000001010ccc140e766b5dbc884ea2d780c5e91e4eb77597ae64288a42575228b79e234900000000000000000002bd37060000000000225120245091249f4f29d30820e5f36e1e5d477dc3386144220bd6f35839e94de4b9cae81c00000000000016001416d31d7632aa17b3b316b813c0a3177f5b6150200140838a1f0f1ee607b54abf0a3f55792f6f8d09c3eb7a9fa46cd4976f2137ca2e3f4a901e314e1b827c3332d7e1865ffe1d7ff5f5d7576a9000f354487a09de44cd00000000'
    # Call your decode_transaction function
    (version, num_inputs, inputs, num_outputs, outputs, locktime) = decode_transaction(raw_tx)
    print(version)

    # Assert that the outputs are as expected
    assert version == '00000002', f'Expected version to be 00000002, but got {version}'
    assert num_inputs == 1, f'Expected num_inputs to be 1, but got {num_inputs}'
    assert len(inputs) == num_inputs, f'Expected {num_inputs} inputs, but got {len(inputs)}'
    assert num_outputs == 2, f'Expected num_outputs to be 2, but got {num_outputs}'
    assert len(outputs) == num_outputs, f'Expected {num_outputs} outputs, but got {len(outputs)}'
    assert locktime == '00000000', f'Expected locktime to be 00000000, but got {locktime}'

# Call the test function
test_decode_transaction()
