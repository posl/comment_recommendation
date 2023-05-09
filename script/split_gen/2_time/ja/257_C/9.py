def main():
    n = int(input())
    s = input()
    w = list(map(int, input().split()))
    #print(n, s, w)
    #print(len(s), len(w), n)
    # 体重の小さい順にソート
    # 体重が同じ人は、sの値が小さい順にソート
    # 体重が同じ人は、sの値が小さい順にソート
    w_s = sorted(zip(w, s), key=lambda x: (x[0], x[1]))
    #print(w_s)
    # 体重の小さい順にソートしたリスト
    w_sort = [x[0] for x in w_s]
    #print(w_sort)
    # sの値が小さい順にソートしたリスト
    s_sort = [x[1] for x in w_s]
    #print(s_sort)
    # 体重の小さい順にソートしたリストの中で、sの値が0の人の数
    #print(s_sort.count('0'))
    # 体重の小さい順にソートしたリストの中で、sの値が0の人の数の最大値
    #print(max(s_sort.count('0'), s_sort.count('1')))
    # 体重の小さい順にソートしたリストの中で、sの値が0の人の数の最大値を出力
    print(max(s_sort.count('0'), s_sort.count('1')))
