def main():
    N,Q = map(int,input().split())
    S = input()
    for i in range(Q):
        t,x = map(int,input().split())
        if t == 1:
            S = S[-x:] + S[:-x]
        elif t == 2:
            print(S[x-1])
