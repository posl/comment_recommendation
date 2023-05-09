def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    while max(h) > 0:
        start = 0
        end = 0
        for i in range(N):
            if h[i] > 0:
                start = i
                break
        for i in range(N-1, -1, -1):
            if h[i] > 0:
                end = i
                break
        for i in range(start, end+1):
            h[i] -= 1
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()