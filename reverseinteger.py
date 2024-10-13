def reverseinteger(x):
    x = str(x)
    lenx = len(x)
    nlist = []

    for i in range(0,lenx):
        nlist.append(x[i])

    nlist.reverse()
    outx = int(''.join(nlist))
    return outx

