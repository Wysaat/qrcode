from modes import *
from data import *
import utils

def encode(data, version, mode):
    # determine the number of bits in character count indicator
    length = utils.getcountbits(version, mode)

    if mode == NUMERIC:
        groups = [data[i:i+3] for i in range(0, len(data), 3)]
        last = groups[-1]
        groups = [('0' * (10 - len(bin(int(group))[2:])) +  \
              bin(int(group))[2:]) for group in groups[:-1]]
        if len(last) == 3:
            last = '0' * (10 - len(bin(int(last))[2:])) + bin(int(last))[2:]
        elif len(last) == 2:
            last = '0' * (7 - len(bin(int(last))[2:])) + bin(int(last))[2:]
        else:
            last = '0' * (4 - len(bin(int(last))[2:])) + bin(int(last))[2:]
        groups.append(last)

    elif mode == ALPHANUMERIC:
        values = [alphanumeric.index(aln) for aln in data]
	groups = [values[i:i+2] for i in range(0, len(values), 2)]
	last = groups[-1]
	groups = [(group[0] * 45 + group[1]) for group in groups[:-1]]
	groups = ['0' * (11 - len(bin(group)[2:])) + bin(group)[2:] \
		  for group in groups]
	if len(last) == 2:
	    last = last[0] * 45 + last[1]
	    llen = 11
	else:
	    last = last[0]
	    llen = 6
	last = '0' * (llen - len(bin(last)[2:])) + bin(last)[2:]
        groups.append(last)

    elif mode == EIGHTBITBYTE:
	values = [(eightbitbyte.index(ebb) + 33) for ebb in data]
	groups = [('0' * (8 - len(bin(value)[2:])) + bin(value)[2:]) \
		  for value in values]

    result = utils.getbitstream(data, length, mode, groups)
    return result
