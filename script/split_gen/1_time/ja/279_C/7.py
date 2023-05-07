def main():
    H,W=map(int,input().split())
    S=[input() for _ in range(H)]
    T=[input() for _ in range(H)]
    def check(S,T):
        for i in range(H):
            for j in range(W):
                if S[i][j]!=T[i][j]:
                    return False
        return True
    for i in range(W):
        for j in range(W):
            S2=[S[i][j] for i in range(H)]
            T2=[T[i][j] for i in range(H)]
            S2.sort()
            T2.sort()
            if S2==T2:
                if check(S,T):
                    print("Yes")
                    exit()
    print("No")
