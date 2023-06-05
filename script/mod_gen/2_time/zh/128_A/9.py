def main():
    # 读入数据
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    bc = [list(map(int, input().split())) for _ in range(m)]
    # 贪心算法
    a.sort()
    bc.sort(key=lambda x: x[1], reverse=True)
    p = 0
    for b, c in bc:
        for _ in range(b):
            if p >= n or a[p] >= c:
                break
            a[p] = c
            p += 1
    print(sum(a))

if __name__ == '__main__':
    main()