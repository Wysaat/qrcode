from modes import *
from data import *

def getcountbits(version, mode):
    """ determine the number of bits in character count indicator """
    if mode == NUMERIC:
	if version in range(1, 10):
	    length = 10
	elif version in range(10, 27):
	    length = 12
	else:
	    length = 14
    elif mode == ALPHANUMERIC:
	if version in range(1, 10):
	    length = 9
	elif version in range(10, 27):
	    length = 11
	else:
	    length = 13
    elif mode == EIGHTBITBYTE:
	if version in range(1, 10):
	    length = 8
	else:
	    length = 16
    elif mode == KANJI:
	if version in range(1, 10):
	    length = 8
	elif version in range(10, 27):
	    length = 10
	else:
	    length = 12
    return length

def getbitstream(data, length, mode, groups):
    count = '0' * (length - len(bin(len(data))[2:])) + bin(len(data))[2:]
    result = mode + count
    for group in groups:
	result += group
    return result

def getversion(data, mode):
    """ a rough estimation of the version to use,
        ensuring highest error correction level """
    size = len(data)
    
    if mode == NUMERIC:
	version = int(size / 19) + 1
    elif mode == ALPHANUMERIC:
	version = int(size / 10) + 1
    elif mode == EIGHTBITBYTE:
	version = int(size / 7) + 1
    
    return version

def genformatinfo(ecl, maskpattern):
    if ecl == 'L':   fbits = '01'
    elif ecl == 'M': fbits = '00'
    elif ecl == 'Q': fbits = '11'
    else:            fbits = '10'
    databits = fbits + maskpattern
    # generator polynomial G(x)'s coefficients
    genpol = [10, 8, 5, 4, 2, 1, 0]
    bins = [int(i) for i in databits]
    bins.reverse()
    pol = [i for i in range(len(bins)) if bins[i] = 1]
    raisedpol = [(i + 10) for i in pol]


