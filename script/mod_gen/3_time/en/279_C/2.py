def main():
    H, W = map(int, input().split())
    S = []
    T = []
    for i in range(H):
        S.append(input())
    for i in range(H):
        T.append(input())
    S = sorted(S)
    T = sorted(T)
    for i in range(H):
        if S[i] != T[i]:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()