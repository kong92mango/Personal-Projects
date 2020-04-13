# pc = [  (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 10)  ]

pc = [ (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 10), (11, 2) ]

dic = {}

for par in pc:
    c = par[1]
    p = par[0]
    try:
        dic[p] += 0
    except:
        dic[p] = 0
    try:
        dic[c] += 1
    except:
        dic[c] = 1

zeros = []
ones = []
for entry in dic:
    if dic[entry] == 0:
        zeros.append(entry)
    elif dic[entry] == 1:
        ones.append(entry)

print (zeros, ones)

#----------------------------------------------------------

for par in pc:
    c = par[1]
    p = par[0]
    if p not in dic:
        dic[p] = []
    try:
        dic[c].append(p)
    except:
        dic[c] = [p]

def getallp(a):
    allP = []
    for p in dic[a]:
        allP.append(p)
        allP += getallp(p)
    return allP

def haveCommonP(a, b):
    ap = getallp(a)
    bp = getallp(b)
    if any(x in ap for x in bp):
        print ("True")
        return
    print("False")

#-------------------------------------------------------------------------

def getearliestp(a, r = False):
    if dic[a] == []:
        if not r:
            print(-1)
        else:
            print(a)
    for p in dic[a]:
        getearliestp(p, r = True)
    return

getearliestp(1)
