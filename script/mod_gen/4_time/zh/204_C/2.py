def main():
    n, m = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    for i in range(m):
        a[i] -= 1
        b[i] -= 1
    ans = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                cnt = 0
                for k in range(m):
                    if a[k] == i and b[k] == j:
                        cnt += 1
                ans += cnt * (cnt - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()