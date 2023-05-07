def main():
    N,Q = list(map(int,input().split()))
    S = input()
    S = list(S)
    for i in range(Q):
        t,x = list(map(int,input().split()))
        if t == 1:
            S.insert(0,S.pop(x-1))
        else:
            print(S[x-1])
