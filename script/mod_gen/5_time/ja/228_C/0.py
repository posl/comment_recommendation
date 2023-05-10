def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for i in range(N)]
    # print(N, K, P)
    for i in range(N):
        # print(i)
        if sum(P[i]) >= K:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()