def main():
    n = int(input())
    s = input()
    ans = [0 for _ in range(n-1)]
    for i in range(n-1):
        l = 0
        while i+l < n-1 and s[l] != s[i+l]:
            l += 1
        ans[i] = l
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()