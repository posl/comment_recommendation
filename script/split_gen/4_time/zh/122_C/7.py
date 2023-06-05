def main():
    N, Q = map(int, input().split())
    S = input()
    l = []
    r = []
    for i in range(Q):
        l1, r1 = map(int, input().split())
        l.append(l1)
        r.append(r1)
    for i in range(Q):
        print(S[l[i]-1:r[i]].count("AC"))
