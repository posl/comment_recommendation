def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N):
        if i < K % N:
            print(K // N + 1)
        else:
            print(K // N)

if __name__ == '__main__':
    main()