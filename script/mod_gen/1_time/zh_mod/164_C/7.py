def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    ans = 1
    for i in range(1,n):
        if s[i] != s[i-1]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()