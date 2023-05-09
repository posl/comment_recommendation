def main():
    H, W = map(int, input().split())
    S = []
    T = []
    for i in range(H):
        S.append(input())
    for i in range(H):
        T.append(input())
    print(S)
    print(T)
    S = sorted(S)
    T = sorted(T)
    print(S)
    print(T)
    if S == T:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()