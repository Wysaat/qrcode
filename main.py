import sys
from modes import *
from data import *
import encode
import utils
import matrix
import errorcode
import draw

if (len(sys.argv) < 3) or (sys.argv[-1] not in ['L', 'M', 'Q', 'H']):
    print "usage: main data_to_encode error_correction_level"
    print "       error_correction_level can be L, M, Q, or H"
    sys.exit(0)
rawdata = sys.argv[1:-1]
ecl = sys.argv[-1]
data = ' '.join(rawdata)

# step 1. data analysis
if set(data).issubset(set(numeric)):
    mode = NUMERIC
elif set(data).issubset(set(alphanumeric)):
    mode = ALPHANUMERIC
elif set(data).issubset(set(eightbitbyte)):
    mode = EIGHTBITBYTE
print "mode determined... is", mode

version = utils.getversion(data, mode)
print "version dtermined... is", version

print "generating codewords now... please wait"
codewords = encode.encode(data, version, mode, ecl)

print "generating finalmessage now... please wait"
finalmessage = errorcode.genfinalmessage(codewords, version, ecl)

print "generating matrix now... please wait"
fmatrix = matrix.getmatrix(version, finalmessage, ecl)

print "draw the qrcode now... please wait"
draw.drawmatrix(fmatrix)
print "..."
print "done!"
