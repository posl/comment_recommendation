def main():
    N,Q = map(int,input().split())
    S = input()
    l = []
    r = []
    for i in range(Q):
        l_i,r_i = map(int,input().split())
        l.append(l_i)
        r.append(r_i)
    for i in range(Q):
        print(S[l[i]-1:r[i]].count("AC"))
