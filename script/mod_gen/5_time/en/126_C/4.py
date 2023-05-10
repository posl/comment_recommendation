def main():
    N, K = map(int, input().split())
    p = 0
    for i in range(1, N+1):
        if i >= K:
            p += 1/N
        else:
            count = 0
            while i < K:
                i *= 2
                count += 1
            p += (1/N)*((1/2)**count)
    print(p)

if __name__ == '__main__':
    main()