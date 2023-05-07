def main():
    n = int(input())
    s = input()
    ans = [0] * (n-1)
    for i in range(1, n):
        for j in range(n-i):
            if s[j] != s[j+i]:
                ans[i-1] = i
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()