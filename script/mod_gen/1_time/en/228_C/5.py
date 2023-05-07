def main():
    N, K = map(int, input().split())
    P = [[int(i) for i in input().split()] for j in range(N)]
    for i in range(N):
        if sum(P[i]) + 100 * (3 - P[i].count(300)) >= 400 * K:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()