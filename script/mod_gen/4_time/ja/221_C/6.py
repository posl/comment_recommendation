def main():
    n = int(input())
    ans = 0
    for i in range(1, n):
        a = i
        b = n - i
        a = str(a)
        b = str(b)
        if '0' in a:
            continue
        if '0' in b:
            continue
        num = 1
        for j in range(len(a)):
            num *= int(a[j])
        for j in range(len(b)):
            num *= int(b[j])
        ans = max(ans, num)
    print(ans)

if __name__ == '__main__':
    main()