def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    k = K // N
    m = K % N
    for i in range(N):
        if i < m:
            print(k + 1)
        else:
            print(k)

if __name__ == '__main__':
    main()