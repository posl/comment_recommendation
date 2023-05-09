def main():
    K = int(input())
    # 2のべき乗表
    powers = []
    n = 1
    while n <= K:
        powers.append(n)
        n *= 2
    # 2のべき乗を使って計算
    ans = ""
    for p in reversed(powers):
        if p <= K:
            ans += "2"
            K -= p
        else:
            ans += "0"
    print(ans)

if __name__ == '__main__':
    main()