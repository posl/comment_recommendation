def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if p[i] == i:
            ans += 1
            if i+1 < n:
                p[i], p[i+1] = p[i+1], p[i]
    print(ans)

if __name__ == '__main__':
    main()