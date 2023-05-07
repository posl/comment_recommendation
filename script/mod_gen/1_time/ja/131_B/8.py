def solve():
    # -*- coding: utf-8 -*-
    # 整数の入力
    N, L = map(int, input().split())
    # print(N, L)
    sum = 0
    min = 10000
    for i in range(N):
        sum += L + i
        if abs(L + i) < min:
            min = abs(L + i)
    # print(sum, min)
    if L >= 0:
        print(sum - min)
    elif L + N - 1 <= 0:
        print(sum - (L + N - 1))
    else:
        print(sum)

if __name__ == '__main__':
    solve()