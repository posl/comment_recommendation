def main():
    N, M = map(int, input().split())
    S = list(map(str, input().split()))
    T = list(map(str, input().split()))
    for i in range(0, N):
        if S[i] in T:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()