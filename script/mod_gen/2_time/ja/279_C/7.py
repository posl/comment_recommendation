def main():
    H,W = map(int,input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    S1 = ["".join(sorted([S[i][j] for i in range(H)])) for j in range(W)]
    T1 = ["".join(sorted([T[i][j] for i in range(H)])) for j in range(W)]
    if S1 == T1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()