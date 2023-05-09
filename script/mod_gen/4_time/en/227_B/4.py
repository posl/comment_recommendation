def main():
    n = int(input())
    s = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            a = s[i]
            b = s[j]
            if 4*a*b+3*a+3*b in s:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()