def main():
    N, M = map(int, input().split())
    S = list(input().split())
    T = list(input().split())
    for i in range(1, N + 1):
        if S[i - 1] in T:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()