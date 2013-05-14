import sys
from modes import *
from data import *
import encode
import messagegeneration
import utils
import matrix

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
codewords = encode.encode(data, version, mode)

# step 3. error correction encoding
ecc = genecc(codewords, version, ecl, necb)
# step 4. codeword generation

# final message generation
finalmessage = 


# step 5. structure final message

# step 6. module placement in the matrix
fmatrix = matrix.place()

# step 7. masking

# step 8. format and version information
