import sys
from modes import *
from data import *
import encode
import utils
import matrix
import errorcode

if len(sys.argv) != 3:
    print "usage: main data_to_encode error_correction_level"
    sys.exit(0)
rawdata = sys.argv[1]
ecl = sys.argv[2]
data = ' '.join(rawdata)

# step 1. data analysis
if set(data).issubset(set(numeric)):
    mode = NUMERIC
elif set(data).issubset(set(alphanumeric)):
    mode = ALPHANUMERIC
elif set(data).issubset(set(eightbitbyte)):
    mode = EIGHTBITBYTE

version = utils.getversion(data, mode)

codewords = encode.encode(data, version, mode, ecl)

finalmessage = errorcode.genfinalmessage(codewords, version, ecl)

fmatrix = matrix.getmatrix(version, finalmessage, ecl)
