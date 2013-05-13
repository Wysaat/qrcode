from modes import *
from data import *

def encode(data, version, mode):
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
    # convert character count indicator to 10 bits for versions 1 to 9
    if version in range(1, 10):
	length = 10
    # convert to 12 bits for versions 10 to 26
    elif version in range(10, 27):
	length = 12
    # convert to 14 bits for versions 27 to 40
    else:
	length = 14
    count = '0' * (length - len(bin(len(data))[2:])) + bin(len(data))[2:]
    result = mode + count
    for group in groups:
        result += group
    return result

    elif mode == ALPHANUMERIC:
        values = [alphanumeric.index(aln) for aln in data]
	groups = [values[i:i+2] for i in range(0, len(values), 2)]
	last = groups[-1]
	decis = [sum(group) for group in groups]
