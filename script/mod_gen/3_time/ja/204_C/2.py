def main():
    n, m = map(int, input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    ans = n * (n-1) // 2
    print(ans)

if __name__ == '__main__':
    main()