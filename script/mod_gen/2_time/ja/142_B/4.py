def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if h[i] >= K:
            count = count + 1
    print(count)

if __name__ == '__main__':
    main()