def main():
    N, M = map(int, input().split())
    S = []
    T = []
    for i in range(N):
        S.append(input())
    for i in range(M):
        T.append(input())
    print(S)
    print(T)

if __name__ == '__main__':
    main()