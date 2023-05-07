def main():
    a, n = map(int, input().split())
    # 1桁の時の計算
    if n < 10:
        if n == 1:
            print(0)
        elif n % a == 0:
            print(1)
        else:
            print(-1)
        return
    # 2桁以上の時の計算
    # 2桁目以降の計算
    ans = 1
    while True:
        ans += 1
        n = int(str(n)[-1] + str(n * a)[-1])
        if n % a != 0:
            print(-1)
            return
        if n == 10:
            n = 1
        if n == 1:
            break
    print(ans)

if __name__ == '__main__':
    main()