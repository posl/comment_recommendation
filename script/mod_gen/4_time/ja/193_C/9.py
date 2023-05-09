def main():
    N = int(input())
    ans = N - 1
    # 2^b で表せる数を引いていく
    b = 2
    while b * b <= N:
        # 2^b で表せる数
        x = b * b
        while x <= N:
            ans -= 1
            x *= b
        b += 1
    print(ans)

if __name__ == '__main__':
    main()