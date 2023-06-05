def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    k = K // N
    r = K % N
    for i in range(N):
        if i < r:
            print(k + 1)
        else:
            print(k)

if __name__ == '__main__':
    main()