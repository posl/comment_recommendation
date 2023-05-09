def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 2で割れる回数
    count_2 = 0
    for a in A:
        while a%2 == 0:
            a = a//2
            count_2 += 1
    # 3で割れる回数
    count_3 = 0
    for a in A:
        while a%3 == 0:
            a = a//3
            count_3 += 1
    # 2で割れる回数と3で割れる回数が同じなら、すべてのa_iを2で割った回数と3で割った回数の合計で、最小の操作回数となる
    if count_2 == count_3:
        print(count_2 + count_3)
    else:
        print(-1)
