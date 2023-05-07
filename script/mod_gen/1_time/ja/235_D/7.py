def main():
    a, n = list(map(int, input().split()))
    q = [1]
    v = [0] * (n + 1)
    v[1] = 1
    while q:
        x = q.pop(0)
        if x == n:
            print(v[x] - 1)
            return
        if x * a <= n and v[x * a] == 0:
            q.append(x * a)
            v[x * a] = v[x] + 1
        if x % 10 != 0 and v[x * 10 + x % 10] == 0:
            q.append(x * 10 + x % 10)
            v[x * 10 + x % 10] = v[x] + 1
    print(-1)

if __name__ == '__main__':
    main()