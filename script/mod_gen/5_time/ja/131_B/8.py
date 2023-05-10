def solve():
    # -*- coding: utf-8 -*-
    # 整数の入力
    n,l = map(int, input().split())
    sum = 0
    min = 1000
    for i in range(n):
        sum += l + i
        if abs(l+i) < min:
            min = abs(l+i)
    if l >= 0:
        sum -= min
    elif l < 0 and l+n-1 > 0:
        sum += min
    else:
        sum -= min
    print(sum)

if __name__ == '__main__':
    solve()