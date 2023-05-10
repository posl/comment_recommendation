def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    now = 1
    for i in range(K):
        now = A[now - 1]
    print(now)

if __name__ == '__main__':
    main()