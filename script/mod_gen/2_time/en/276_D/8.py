def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 2で割り切れる回数
    # 3で割り切れる回数
    # 2と3の最小公倍数で割り切れる回数
    cnt2 = 0
    cnt3 = 0
    cnt23 = 0
    for a in A:
        while a % 2 == 0:
            cnt2 += 1
            a //= 2
        while a % 3 == 0:
            cnt3 += 1
            a //= 3
    # 2と3の最小公倍数で割り切れる回数を求める
    for a in A:
        while a % 2 == 0 or a % 3 == 0:
            if a % 2 == 0:
                a //= 2
            if a % 3 == 0:
                a //= 3
        if a != 1:
            print(-1)
            return
    # 2と3の最小公倍数で割り切れる回数を求める
    for a in A:
        while a % 2 == 0 or a % 3 == 0:
            if a % 2 == 0:
                a //= 2
            if a % 3 == 0:
                a //= 3
        if a != 1:
            print(-1)
            return
    print(abs(cnt2 - cnt3))

if __name__ == '__main__':
    main()