def main():
    n = int(input())
    s = input()
    ans = [0 for i in range(n-1)]
    for i in range(1,n):
        for j in range(n-i):
            if s[j] != s[j+i]:
                ans[i-1] += 1
    for i in range(n-1):
        print(ans[i])

if __name__ == '__main__':
    main()