def main():
    k = int(input())
    s = input()
    t = input()
    #print(k, s, t)
    sc = [0]*10
    tc = [0]*10
    for i in range(4):
        sc[int(s[i])] += 1
        tc[int(t[i])] += 1
    #print(sc, tc)
    #print(sc.index(max(sc)), tc.index(max(tc)))
    #print(sc[sc.index(max(sc))], tc[tc.index(max(tc))])
    #print(sc[sc.index(max(sc))] + tc[tc.index(max(tc))])
    if sc[sc.index(max(sc))] + tc[tc.index(max(tc))] > k:
        print(0)
        return
    else:
        #print(sc[sc.index(max(sc))], tc[tc.index(max(tc))])
        #print(k - sc[sc.index(max(sc))] - tc[tc.index(max(tc))])
        #print(9*k - 8)
        #print(9*k - 8 - sc[sc.index(max(sc))] - tc[tc.index(max(tc))])
        #print(9*k - 8 - sc[sc.index(max(sc))] - tc[tc.index(max(tc))])
        #print(9*k - 8 - sc[sc.index(max(sc))] - tc[tc.index(max(tc))])
        #print(9*k - 8 - sc[sc.index(max(sc))] - tc[tc.index(max(tc))])
        #print(9*k - 8 - sc[sc.index(max(sc))] - tc[tc.index(max(tc))])
        #print(9*k - 8 - sc[sc.index(max(sc))] - tc[tc.index(max(tc))])
        #print(9*k - 8 - sc[sc.index(max(sc))] - tc[tc.index(max(tc))])
        #print(9*k - 8 - sc[sc.index(max(sc))] - tc[tc.index(max(tc))])
        #print(9*k - 8 - sc[sc.index(max(sc))] - tc[tc.index(max(tc))])
        print((9*k - 8 - sc[sc.index(max(sc))] - tc[tc.index(max(tc))])/(9*k - 8))
        return
