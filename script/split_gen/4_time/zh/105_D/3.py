def solve(n,m,alist):
    #alist的前缀和
    sumalist = [0]
    for i in range(n):
        sumalist.append(sumalist[i]+alist[i])
    #print(sumalist)
    #alist的前缀和的模m的余数
    modlist = [0]
    for i in range(n):
        modlist.append(sumalist[i+1]%m)
    #print(modlist)
    #modlist中的模m的余数的次数统计
    moddict = {}
    for i in modlist:
        if i in moddict:
            moddict[i] += 1
        else:
            moddict[i] = 1
    #print(moddict)
    #moddict的value中的模m的余数的次数统计
    moddict2 = {}
    for i in moddict.values():
        if i in moddict2:
            moddict2[i] += 1
        else:
            moddict2[i] = 1
    #print(moddict2)
    #moddict2中的模m的余数的次数统计
    moddict3 = {}
    for i in moddict2.values():
        if i in moddict3:
            moddict3[i] += 1
        else:
            moddict3[i] = 1
    #print(moddict3)
    #moddict3中的模m的余数的次数统计
    moddict4 = {}
    for i in moddict3.values():
        if i in moddict4:
            moddict4[i] += 1
        else:
            moddict4[i] = 1
    #print(moddict4)
    #moddict4中的模m的余数的次数统计
    moddict5 = {}
    for i in moddict4.values():
        if i in moddict5:
            moddict5[i] += 1
        else:
            moddict5[i] = 1
    #print(moddict5)
    #moddict5中的模m的余数的次数统计
    moddict6 = {}
    for i in moddict5.values():
        if i in moddict6:
            moddict6[i] += 1
        else:
            moddict6[i]
