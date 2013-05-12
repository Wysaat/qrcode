from modes import *

def encode(data, mode):
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
    # convert character count indicator to 10 bits for version 1-H
    count = '0' * (10 - len(bin(len(data))[2:])) + bin(len(data))[2:]
    result = mode + count
    for group in groups:
        result += group
    return result
