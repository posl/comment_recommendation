def main():
    N, M = map(int, input().split())
    S = list(input().split())
    T = list(input().split())
    for i in range(N):
        if S[i] in T:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()