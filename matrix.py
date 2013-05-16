from gendata import *
import utils
# queit zone size
sqz = 5

# matrix made up of 
getmatrix(version, finalmessage, ecl, maskpattern):
    size = matrixsizedict[version]
    remainderbits = remnumdict[version]
    matrix = [[-1  for i in range(size + sqz * 2)]
	    for j in range(size +  sqz * 2)]

    # 1. add finder pattern and separators
    # upper left
    for i in range(8):
	for j in range(8):
	    matrix[i][j] = 0
    for i in range(7):
	for j in range(7):
	    matrix[i][j] = 1
    for i in range(1, 6):
	for j in range(1, 6):
	    matrix[i][j] = 0
    for i in range(2, 5):
	for j in range(2, 5):
	    matrix[i][j] = 1

    # upper right
    for i in range(size - 8, size):
	for j in range(8):
	    matrix[i][j] = 0
    for i in range(size - 7, size):
	for j in range(7):
	    matrix[i][j] = 1
    for i in range(size - 6, size - 1):
	for j in range(1, 6):
	    matrix[i][j] = 0
    for i in range(size - 5, size - 2):
	for j in range(2, 5):
	    matrix[i][j] = 1

    # lower left
    for i in range(8):
	for j in range(size - 8, size):
	    matrix[i][j] = 0
    for i in range(7):
	for j in range(size - 7, size):
	    matrix[i][j] = 1
    for i in range(1, 6):
	for j in range(size - 6, size -1):
	    matrix[i][j] = 0
    for i in range(2, 5):
	for j in range(size - 5, size -2):
	    matrix[i][j] = 1

    # 2. add timing patterns
    for i in range(8, size - 8, 2):
	matrix[i][6] = 1
	matrix[i + 1][6] = 0
    for j in range(8, size - 8, 2):
	matrix[6][j] = 1
	matrix[6][j + 1] = 0

    # 3. add alignment patterns(version 1 doesn't need)
    if version != 1:
        cents = aligndict[version]
        for centx in cents:
	    for centy in cents:
	        if not ((centx in range(8) and centy in range(8)) or
		        (centx in range(size -8, size) and centy in range(8)) or
		        (centx in range(8) and centy in range(size -8, size))):
		    for i in range(centx - 2, centx + 3):
		        for j in range(centy - 2, centy + 3):
			    matrix[i][j] = 1
		    for i in range(centx - 1, centx + 2):
		        for j in range(centy -1, centy + 2):
			    matrix[i][j] = 0
		    matrix[centx][centy] = 1

    # 4. add format information
    formatinfo = utils.genformatinfo(ecl, maskpattern)
    for j in range(6):
        matrix[8, j] = formatinfo[j]
    matrix[7, 8] = formatinfo[6]
    for j in range(size - 8, size):
        matrix[8, j] = formatinfo[j - size + 15]

    for i in range(size - 1, size - 8, -1):
        matrix[i, 8] = formatinfo[size - 1 - i]
    matrix[size - 8, 8] = 1 # this position should always be dark
    matrix[8, 8] = formatinfo[7]
    matrix[7, 8] = formatinfo[8]
    for i in range(6):
        matrix[i, 8] = formatinfo[-(i + 1)]

    # 5. add version information(for versions 7-40 only)
    if version > 6:
        versioninfo = versioninfodict[version]
        # upper right
        n = len(versioninfo) - 1
        for i in range(6):
            for j in range(size - 11, size - 8):
                matrix[i][j] = versioninfo[n]
                n -= 1

        # lower left
        n = len(versioninfo) - 1
        for j in range(6):
            for i in range(size - 11, size - 8):
                matrix[i][j] = versioninfo[n]
                n -= 1

    # 6. add final message
    while True:
        if matrix[i][j] == -1:
            matrix[i][j] = int(finalmessage[0])
            finalmessage = finalmessage.lstrip(finalmessage[0])
            if rank == 7 or rank == 5:
                if matrix[i][j - 1] == -1:
                    j -= 1
                else:
                    i -= 1
            if rank == 6 or rank == 4:
                if matrix[i - 1][j + 1] == -1:
                    i -= 1
                    j += 1
                elif matrix[i - 1][j] == -1:
                    i -= 1
                else:
