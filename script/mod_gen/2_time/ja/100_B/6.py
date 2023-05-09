def main():
    # A: 100で何回割り切れるか
    # B: N番目に小さいもの
    A, B = map(int, input().split())
    # 100でA回割り切れる数を求める
    ans = 100**A
    # 100でA回割り切れる数の中でB番目に小さい数を求める
    for i in range(1, B):
        ans += 100**A
    print(ans)

if __name__ == '__main__':
    main()