# generate data from tables in the iso/iec standard

# get total data capacity, store in capdict
# remainder bits of each version is in the last column of table 1
# store remainder numbers in remnumdict
with open("table1.txt") as f:
    lines = f.readlines()
    capdict = {}
    remnumdict = {}
    matrixsizedict = {}
    for line in lines:
	capdict[int(line.split()[0])] = int(line.split()[-2])
	remnumdict[int(line.split()[0])] = int(line.split()[-1])
        matrixsizedict[int(line.split()[0])] = int(line.split()[1])

# get input data number corresponding to version, error
# correciton level
# store in
with open("tables7to11.txt") as f:
    lines = f.readlines()
    datanumdict = {}
    lines = [line.split() for line in lines]
    lines = [line for line in lines if line != []]
    newlines = []
    for line in lines:
	if len(line) > 1:
	    if line[0].isdigit():
	        newlines.append(line[1:])
	    else:
	        newlines.append(line)
    lines = newlines
    for i in range(1, 41):
	datanumdict[(i, 'Q')] = int(lines[4 * (i - 1) + 0][1])
	datanumdict[(i, 'H')] = int(lines[4 * (i - 1) + 1][1])
	datanumdict[(i, 'M')] = int(lines[4 * (i - 1) + 2][1])
	datanumdict[(i, 'L')] = int(lines[4 * (i - 1) + 3][1])

# alignment patterns data
with open("tableE1.txt") as f:
    aligndict = {}
    lines = f.readlines()
    lines = [line.split() for line in lines]
    for line in lines:
	line = [int(i) for i in line]
	aligndict[line[0]] = line[2:]

# version information
with open("tableD1.txt") as f:
    versioninfodict = {}
    lines = f.readlines()
    lines = [line.split() for line in lines]
    lines = [line for line in lines if line != []]
    for line in lines:
        versioninfodict[int(line[0])] = line[1] + line[2] + line[3] \
                                          + line[4] + line[5]

# error correction codewords data
with open("thonky1.txt") as f:
    diceccw = {}
    lines = f.readlines()
    lines = [line.split('(')[0] for line in lines]
    lines = [line.split() for line in lines]
    lines = [line for line in lines if len(line) > 0]
    for line in lines:
	data = [int(i) for i in line[1:]]
	diceccw[line[0]] = data

with open('thonky2.txt') as f:
    exptoint = {}
    inttoexp = {}
    lines = f.readlines()
    lines = [line.split() for line in lines]
    for line in lines:
	exptoint[int(line[0])] = int(line[1])
    for line in lines[1:]:
	inttoexp[int(line[2])] = int(line[3])


