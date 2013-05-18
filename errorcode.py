from gendata import *

def gengenpol(length):
    p1, p2 = [0, 0], [0, 1]
    for times in range(length - 1):
	result = []
	for i in range(len(p2)):
	    for j in range(len(p1)):
		result.append((p1[j] + p2[i]) % 255)
	comb1 = result[1:len(p1)]
	comb2 = result[len(p1):(len(result) - 1)]
	comb1 = [exptoint[i] for i in comb1]
	comb2 = [exptoint[i] for i in comb2]
	combed = [i[0] ^ i[1] for i in zip(comb1, comb2)]
	combed = [inttoexp[i] for i in combed]
	p1 = [result[0]] + combed + [result[-1]]
        p2[1] += 1
    return p1

def geneccodewords(codewords, version, ecl):
    key = str(version) + '-' + ecl
    data = diceccw[key]
    eccs = []
    genpol = gengenpol(data[1])
    lcodewords = []
    for i in range(data[2]):
	lcodewords.append(codewords[i * data[3] : (i + 1) * data[3]])
    if len(data) == 6:
	base = data[0] - data[2] * data[3]
	for i in range(data[4]):
	    lcodewords.append(codewords[base + i * data[5] : 
		base + (i + 1) * data[5]])
    for codewords in lcodewords:
        mespol = [int(cw, 2) for cw in codewords]
	times = len(mespol)
	for i in range(times):
	    # step 1. multiply the generator polynomial by the lead term
	    # of the xor result from the previous step
	    lead = inttoexp[mespol[0]]
	    result = [((i + lead) % 255) for i in genpol]
	    result = [exptoint[i] for i in result]

	    if len(mespol) > len(result):
	        result.extend([0] * (len(mespol) - len(result)))
	    else:
		mespol.extend([0] * (len(result) - len(mespol)))

	    # step 2. xor the result with the last result
            mespol = [i[0] ^ i[1] for i in zip(result, mespol)]
	    # drop leading 0 term
	    mespol = mespol[1:]
	    print mespol
	ewords = ['0' * (8 - len(bin(i)[2:])) + bin(i)[2:] 
		for i in mespol]
	eccs.append(ewords)
    return eccs
