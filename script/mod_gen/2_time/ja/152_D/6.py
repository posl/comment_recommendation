def main():
    N = int(input())
    ans = 0
    # 0~9の数のリストを作成
    num = [0,0,0,0,0,0,0,0,0,0]
    for i in range(1,N+1):
        # 一桁目と一番下の桁の数字を取得
        first = int(str(i)[0])
        last = int(str(i)[-1])
        # 一桁目の数字のリストの要素に1を足す
        num[first] += 1
        # 一番下の桁の数字のリストの要素に1を足す
        num[last] += 1
    # 0~9の数のリストの要素を2で割る
    for i in range(10):
        num[i] = num[i] // 2
    # 0~9の数のリストの要素を足す
    for i in range(10):
        ans += num[i]
    print(ans)

if __name__ == '__main__':
    main()