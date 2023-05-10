def main():
    n, m = map(int, input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    ans = 0
    for i in range(m):
        for j in range(m):
            if a[i] == b[j]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()