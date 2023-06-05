def main():
    n = int(input())
    h = list(map(int, input().split()))
    h.append(0)
    h.reverse()
    ans = 0
    now = 0
    for i in range(n):
        if now < h[i]:
            ans += 1
            now = h[i]
    print(ans)

if __name__ == '__main__':
    main()