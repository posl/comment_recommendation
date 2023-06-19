def main():
    N, M = map(int, input().split())
    k = [0] * M
    a = [[] for _ in range(M)]
    for i in range(M):
        k[i] = int(input())
        a[i] = list(map(int, input().split()))
    print(solve(N, M, k, a))

if __name__ == '__main__':
    main()