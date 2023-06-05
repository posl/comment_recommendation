def main():
    # 读取输入
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    bc = []
    for _ in range(m):
        b, c = map(int, input().split())
        bc.append((b, c))
    # 解决
    a.sort()
    bc.sort(key=lambda x: x[1], reverse=True)
    i = 0
    for b, c in bc:
        for _ in range(b):
            if i >= n or a[i] >= c:
                break
            a[i] = c
            i += 1
    print(sum(a))

if __name__ == '__main__':
    main()