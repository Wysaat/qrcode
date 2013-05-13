import sys
from modes import *
from data import *
import encode
import utils

rawdata = sys.argv[1:]
data = ' '.join(rawdata)

# step 1. data analysis
if set(data).issubset(set(numeric)):
    mode = NUMERIC
elif set(data).issubset(set(alphanumeric)):
    mode = ALPHANUMERIC
elif set(data).issubset(set(eightbitbyte)):
    mode = EIGHTBITBYTE

version = utils.getversion(data, mode)

# step 2. data encodation
bitstream = encode.encode(data, version, mode)

# step 3. error correction encoding

# step 4. codeword generation

# step 5. structure final message

# step 6. module placement in the matrix

# step 7. masking

# step 8. format and version information
