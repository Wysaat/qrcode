from copy import deepcopy

def mask(matrix):
    # in the unmasked matrix, 2 means 0, 3 means 1
    matrixes = []
    size = len(matrix)
    matrixes.append(domask(matrix, '(((i + j) % 2) == 0)'))
    matrixes.append(domask(matrix, '((i % 2) == 0)'))
    matrixes.append(domask(matrix, '((j % 3) == 0)'))
    matrixes.append(domask(matrix, '(((i + j) % 3) == 0)'))
    matrixes.append(domask(matrix, '(((int(i / 2) + int(j / 3)) % 2) == 0)'))
    matrixes.append(domask(matrix, '((((i * j) % 2) + ((i * j) % 3)) == 0)'))
    matrixes.append(domask(matrix, '(((((i * j) % 2) + ((i * j) % 3)) % 2) == 0)'))
    matrixes.append(domask(matrix, '(((((i * j) % 3) + ((i + j) % 2)) % 2) == 0)'))
    scores = [scoremasking(matrix) for matrix in matrixes]
    ind = scores.index(max(scores))
    maskpattern = '0' * (3 - len(bin(ind)[2:])) + bin(ind)[2:]
    return matrixes[ind], maskpattern


def domask(matrix, condition):
    nmatrix = deepcopy(matrix)
    for i in range(len(nmatrix)):
	for j in range(len(nmatrix)):
	    if nmatrix[i][j] == 2 and eval(condition):
		nmatrix[i][j] = 1
	    elif nmatrix[i][j] == 3 and not eval(condition):
		nmatrix[i][j] = 1
	    elif nmatrix[i][j] > 1:
		nmatrix[i][j] = 0
    return nmatrix

def scorefeature1(matrix):
    score = 0
    for i in range(len(matrix)):
	string = ''.join(str(matrix[i]))
	ones = [i for i in string.split('0') if len(i) > 5]
	zeros = [i for i in string.split('1') if len(i) > 5]
	for one in ones:
	    score += len(one) - 2
	for zero in zeros:
	    score += len(zero) - 2
    return score

def scorefeature2(matrix):
    score = 0
    for i in range(len(matrix)):
	for j in range(len(matrix)):
	    m = n = 1
	    color = matrix[i][j]
	    while True:
		if i == len(matrix) - 1:
		    break
	        for y in range(n):
		    if matrix[i + 1][j + y] != color:
		        break
	        m += 1
		i += 1
	    while True:
		if j == len(matrix) -1:
		    break
		for x in range(m):
		    if matrix[i - x][j + 1] != color:
			break
		n += 1
		j += 1
	    score += 3 * (m - 1) * (n - 1)
    return score

def scorefeature3(matrix):
    score = 0
    for i in range(len(matrix)):
	string = ''.join(str(matrix[i]))
	if '1011101' in string:
	    score += 40
    return score

def scorefeature4(matrix):
    dark = 0
    for i in range(len(matrix)):
	for j in range(len(matrix)):
	    if matrix[i][j] == 1:
		dark += 1
    proportion = dark / (len(matrix) ** 2)
    deviation = proportion - 0.5
    de = int(deviation * 100)
    k = int(de / 5)
    score = 10 * k
    return score

def scoremasking(matrix):
    score = 0

    # feature 1
    rotmatrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix))]
    score += scorefeature1(matrix)
    score += scorefeature1(rotmatrix)
    
    # feature 2
    score += scorefeature2(matrix)
    
    # feature 3
    score += scorefeature3(matrix)
    score += scorefeature3(rotmatrix)

    # feature 4
    score += scorefeature4(matrix)

    return score
