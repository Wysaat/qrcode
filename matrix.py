from gendata import *
# queit zone size
sqz = 5

# matrix made up of 
getmatrix(version, finalmessage):
    size = matrixsizedict[version]
    remainderbits = remnumdict[version]

    # add quiet zone(size is sqz)
    matrix = [[0  for i in range(size + sqz * 2)]
	    for j in range(size +  sqz * 2)]
    for i in range(sqz, size - sqz):
	for j in range(sqz, size - sqz):
	    matrix[i][j] == -1

    # draw finder pattern and separators
    # 1. upper left
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

    # 2. upper right
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

    # 3. lower left
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
