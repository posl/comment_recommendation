def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        S.append(list(map(int, input().split())))
    for i in range(N):
        T.append(list(map(int, input().split())))
    S = sorted(S)
    T = sorted(T)
    if S == T:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()