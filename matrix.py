from gendata import *

getmatrix(version, finalmessage):
    size = matrixsizedict[version]
    remainderbits = remnumdict[version]
    matrix = [[-1  for i in range(size)] for j in range(size)]
