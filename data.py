numeric = '0123456789'
alphanumeric = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:'
# JIS8 character set from 0x21 to 0x7D(yen replaced by space)
eightbitbyte = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[ ]^_`abcdefghijklmnopqrstuvwxyz{|}'

# padding code words(pcws)
pcws = ['11101100', '00010001']

# data capability for each version is defined in table 1

# input data capability for each (version, error correction level) pair
# is defined in tables 7 to 11

# number of error correction blocks and error correction code numbers per block
# are defined in tables 13 to 22

# the "total number of code words" in tables 13 to 22 are same as those in table 1,
# but are different things from input data capability defined in tables 7 to 11
