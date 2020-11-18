# from base_components import *
# from package_builders import *
from package_encoder import *


if __name__ == "__main__":
    builder = SubackBuilder()
    builder.reset()
    builder.buildFixedHeader()
    builder.buildVariableHeader(10)
    builder.buildPayload([12,36])

    connack = builder.getPackage()

    print(str(connack))

    encoder = GenericPackageEncoder()
    encodedText = encoder.encode(connack)

    displayControlPackageBinary(encodedText)

    decoder = GenericPackageDecoder()
    header = decoder.decodeFixedHeader(encodedText[0:16])
    connack_decoded = decoder.decodeVariableComponents(encodedText[16:], header)

    print(str(connack_decoded))

    if str(connack) == str(connack_decoded):
        print("We got a match!")



