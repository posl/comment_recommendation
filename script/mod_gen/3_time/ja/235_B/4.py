def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i == 0:
            ans += 1
        else:
            if h[i] >= h[i-1]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()