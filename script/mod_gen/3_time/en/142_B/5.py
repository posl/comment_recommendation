def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    c = 0
    for i in range(N):
        if h[i] >= K:
            c += 1
    print(c)

if __name__ == '__main__':
    main()