def main():
    N, M = map(int, input().split())
    p = []
    s = []
    for i in range(M):
        pi, si = input().split()
        p.append(int(pi))
        s.append(si)
    #print(p)
    #print(s)
    #print(N)
    #print(M)
    #正答数
    ac = 0
    #ペナルティ数
    wa = 0
    #問題のACの有無
    ac_list = [False] * N
    #正答数とペナルティ数の計算
    for i in range(M):
        if s[i] == "AC":
            if ac_list[p[i]-1] == False:
                ac_list[p[i]-1] = True
                ac += 1
                wa += 1
        else:
            if ac_list[p[i]-1] == False:
                wa += 1
    print(ac, wa)
