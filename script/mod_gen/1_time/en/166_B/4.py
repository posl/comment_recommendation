def main():
    N, K = map(int, input().split())
    A = []
    for i in range(K):
        d = int(input())
        A += list(map(int, input().split()))
    print(N - len(set(A)))

if __name__ == '__main__':
    main()