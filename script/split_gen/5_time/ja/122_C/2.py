def main():
    N,Q = map(int,input().split())
    S = input()
    AC = [0]*N
    for i in range(1,N):
        if S[i-1] == "A" and S[i] == "C":
            AC[i] = AC[i-1] + 1
        else:
            AC[i] = AC[i-1]
    for i in range(Q):
        l,r = map(int,input().split())
        if l == 1:
            print(AC[r-1])
        else:
            print(AC[r-1] - AC[l-1])
