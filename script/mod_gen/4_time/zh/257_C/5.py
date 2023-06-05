def main():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))
    # 0,1の数を数える
    count_zero = s.count('0')
    count_one = s.count('1')
    # print(count_zero, count_one)
    # 重さの小さい順にソート
    w.sort()
    # print(w)
    # 重さの小さい順に0,1の数を数える
    count_zero_list = []
    count_one_list = []
    tmp_zero = 0
    tmp_one = 0
    for i in range(n):
        if s[i] == '0':
            tmp_zero += 1
        else:
            tmp_one += 1
        count_zero_list.append(tmp_zero)
        count_one_list.append(tmp_one)
    # print(count_zero_list)
    # print(count_one_list)
    # 重さの小さい順に0,1を判定
    max_count = 0
    for i in range(n):
        # 0の数は、0,1の数から引く
        tmp_count_zero = count_zero_list[i] - count_zero
        # 1の数は、0,1の数から引く
        tmp_count_one = count_one_list[i] - count_one
        # print(tmp_count_zero, tmp_count_one)
        # 0,1の数の差の絶対値が最大のものを選ぶ
        tmp_max_count = max(abs(tmp_count_zero), abs(tmp_count_one))
        # print(tmp_max_count)
        # 重さの小さい順に判定しているため、最大値を超える場合は、最大値を更新する
        if tmp_max_count > max_count:
            max_count = tmp_max_count
    print(max_count)

if __name__ == '__main__':
    main()