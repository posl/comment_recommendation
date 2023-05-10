def main():
    N = int(input())
    h = list(map(int, input().split()))
    h.insert(0, 0)
    ans = 0
    for i in range(1, N+1):
        if h[i] > h[i-1]:
            ans += h[i] - h[i-1]
    print(ans)

if __name__ == '__main__':
    main()