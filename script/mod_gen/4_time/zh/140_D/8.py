def main():
    n, k = map(int, input().split())
    s = input()
    num = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            num += 1
    num += min(2*k, n-1)
    print(num)

if __name__ == '__main__':
    main()