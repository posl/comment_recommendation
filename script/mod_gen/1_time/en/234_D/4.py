def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    for i in range(K, N):
        print(sorted(P[:i])[-K])

if __name__ == '__main__':
    main()