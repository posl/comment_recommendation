def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    max_h = 0
    for i in range(n):
        if h[i] >= max_h:
            ans += 1
            max_h = h[i]
    print(ans)

if __name__ == '__main__':
    main()