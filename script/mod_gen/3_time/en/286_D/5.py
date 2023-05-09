def main():
    n, x = map(int, input().split())
    a = [0]*n
    b = [0]*n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    ans = "No"
    for i in range(2**n):
        tmp = 0
        for j in range(n):
            if ((i >> j) & 1):
                tmp += a[j]*b[j]
        if tmp == x:
            ans = "Yes"
    print(ans)

if __name__ == '__main__':
    main()