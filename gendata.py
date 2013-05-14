# generate data from tables in the iso/iec standard

# get total data capacity, store in capdict
# remainder bits of each version is in the last column of table 1
# store remainder numbers in remnumdict
with open("table1.txt") as f:
    lines = f.readlines()
    capdict = {}
    remnumdict = {}
    for line in lines:
	capdict[int(line.split()[0])] = int(line.split()[-2])
	remnumdict[int(line.split()[0])] = int(line.split()[-1])

# get input data number corresponding to version, error
# correciton level
# store in
with open("tables7to11.txt") as f:
    lines = f.readlines()
    datanumdict = {}
    lines = [line.split() for line in lines]
    lines = [line for line in lines if line != []]
    for line in lines:
	if len(line) > 1:
	    if line[0].isdigit():
	        newlines.append(line[1:])
	    else:
	        newlines.append(line)
    lines = newlines
    for i in range(1, 41):
	datanumdict[(i, 'Q')] = lines[4 * (i - 1) + 1][1]
	datanumdict[(i, 'H')] = lines[4 * (i - 1) + 2][1]
	datanumdict[(i, 'M')] = lines[4 * (i - 1) + 3][1]
	datanumdict[(i, 'L')] = lines[4 * (i - 1) + 4][1]

