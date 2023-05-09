def main():
    n = int(input())
    a = list(map(int, input().split()))
    # 1. 約数を求める
    # 2. その約数が、いずれかの数値の倍数であるかどうかを確認する
    # 3. いずれかの数値の倍数である場合、その約数は除外する
    # 4. 除外した約数の数をカウントする
    # 5. 除外した約数の数が、入力数値の数と同じ数値である場合、その数値は、
    #    いずれの数値の倍数でないという条件を満たす
    # 6. その数値をカウントする
    # 7. 最後に、カウントした数値を出力する
    # 1. 約数を求める
    # 1.1. 最大値を求める
    max_a = max(a)
    # 1.2. 最大値の約数を求める
    # 1.2.1. 約数を格納するリスト
    divisor_list = []
    # 1.2.2. 約数を求める
    for i in range(1, max_a + 1):
        if i * i > max_a:
            break
        if max_a % i == 0:
            divisor_list.append(i)
            if i != max_a // i:
                divisor_list.append(max_a // i)
    # 1.2.3. 約数リストをソートする
    divisor_list.sort()
    # 1.3. 約数リストを逆順にする
    divisor_list = divisor_list[::-1]
    # 2. その約数が、いずれかの数値の倍数であるかどうかを確認する
    # 2.1. その約数が、い

if __name__ == '__main__':
    main()