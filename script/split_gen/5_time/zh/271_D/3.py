def solve(n,s,ab):
    #ab = [(1,4),(2,3),(5,7)]
    #n,s = 3,11
    for i in range(2**n):
        #print(i)
        a = []
        for j in range(n):
            if (i>>j)&1:
                a.append(ab[j][0])
            else:
                a.append(ab[j][1])
        #print(a)
        if sum(a) == s:
            print("Yes")
            for j in range(n):
                if (i>>j)&1:
                    print("T",end="")
                else:
                    print("H",end="")
            print()
            return
    print("No")
    return
