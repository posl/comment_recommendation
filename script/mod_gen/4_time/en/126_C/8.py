def main():
    n, k = map(int, input().split())
    if k == 1:
        print(0)
        return
    if n == 1:
        print(1)
        return
    ret = 0
    for i in range(1, n + 1):
        cnt = 0
        while i < k:
            i *= 2
            cnt += 1
        ret += (1 / n) * ((1 / 2) ** cnt)
    print(ret)

if __name__ == '__main__':
    main()