def main():
    N = int(input())
    A = list(map(int, input().split()))
    #最初に全ての合計を出しておく
    sum_all = sum(A)
    #連続する部分列の合計を出しておく
    sum_part = []
    sum_part.append(A[0])
    for i in range(1,N):
        sum_part.append(sum_part[i-1] + A[i])
    #最初の一回目のカットで3つの部分列に分ける
    #最初のカットの場所は1番目からN-2番目までのN-2通り
    min_diff = 10**9
    for i in range(1,N-2):
        #1回目のカットで分けた部分列の合計を出す
        sum_1 = sum_part[i-1]
        sum_2 = sum_part[N-1] - sum_part[i-1]
        #2回目のカットで分けた部分列の合計を出す
        #2回目のカットの場所はi番目からN-1番目までのN-1-i通り
        for j in range(i+1,N-1):
            sum_3 = sum_part[j-1] - sum_part[i-1]
            sum_4 = sum_part[N-1] - sum_part[j-1]
            #最後のカットで分けた部分列の合計を出す
            sum_5 = sum_all - sum_1 - sum_2 - sum_3 - sum_4
            #最大値と最小値を求める
            max_value = max(sum_1,sum_2,sum_3,sum_4,sum_5)
            min_value = min(sum_1,sum_2,sum_3,sum_4,sum_5)
            #最大値と最小値の差を求める
            diff = max_value - min_value
            #最大値と最小値の差の最小値を求める
            min_diff = min(min_diff,diff)
    #結果を出力する
    print(min_diff)

if __name__ == '__main__':
    main()