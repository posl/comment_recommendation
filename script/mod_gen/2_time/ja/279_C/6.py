def main():
    H,W = map(int,input().split())
    S = [input() for h in range(H)]
    T = [input() for h in range(H)]
    if H%2==0 and W%2==0:
        if S==T:
            print("Yes")
            return
        else:
            print("No")
            return
    elif H%2==0:
        S = ["".join(S[h][w] for h in range(H)) for w in range(W)]
        T = ["".join(T[h][w] for h in range(H)) for w in range(W)]
        if S==T:
            print("Yes")
            return
        else:
            print("No")
            return
    elif W%2==0:
        S = ["".join(S[h][w] for w in range(W)) for h in range(H)]
        T = ["".join(T[h][w] for w in range(W)) for h in range(H)]
        if S==T:
            print("Yes")
            return
        else:
            print("No")
            return
    else:
        S = ["".join(S[h][w] for h in range(H)) for w in range(W)]
        T = ["".join(T[h][w] for h in range(H)) for w in range(W)]
        if S==T:
            print("Yes")
            return
        else:
            print("No")
            return

if __name__ == '__main__':
    main()