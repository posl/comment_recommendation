def main():
    N,Q = map(int,input().split())
    S = input()
    l = [0]
    for i in range(1,N):
        if S[i-1] == "A" and S[i] == "C":
            l.append(l[i-1]+1)
        else:
            l.append(l[i-1])
    for _ in range(Q):
        l_i,r_i = map(int,input().split())
        print(l[r_i-1]-l[l_i-1])
