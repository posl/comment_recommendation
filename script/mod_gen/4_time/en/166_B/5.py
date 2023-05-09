def main():
    N, K = map(int, input().split())
    A = []
    for _ in range(K):
        d = int(input())
        A += map(int, input().split())
    print(N - len(set(A)))

if __name__ == '__main__':
    main()