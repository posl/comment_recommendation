def main():
    N, A, B = map(int, input().split())
    # 総和を求める
    sum = 0
    # N 以下の整数であって、A の倍数でも B の倍数でもないものの総和を求めてください。
    for i in range(1, N+1):
        if i % A != 0 and i % B != 0:
            sum += i
    print(sum)

if __name__ == '__main__':
    main()