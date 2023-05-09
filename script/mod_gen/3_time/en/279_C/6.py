def main():
    H, W = list(map(int, input().split()))
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    for i in range(H):
        if sorted(S[i]) != sorted(T[i]):
            print("No")
            return
    for j in range(W):
        if sorted([S[i][j] for i in range(H)]) != sorted([T[i][j] for i in range(H)]):
            print("No")
            return
    print("Yes")
main()

if __name__ == '__main__':
    main()