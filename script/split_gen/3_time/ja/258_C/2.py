def main():
    N,Q = map(int,input().split())
    S = input()
    S = S[::-1]
    for i in range(Q):
        t,x = map(int,input().split())
        if t == 1:
            S = S[x:] + S[:x]
        else:
            print(S[x-1])
