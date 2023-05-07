def main():
    N = int(input())
    xy = [list(map(int, input().split())) for _ in range(N)]
    # 1からNまでの順列を列挙
    import itertools
    p = itertools.permutations(range(N))
    # 順列の組み合わせを全て計算
    import math
    ans = 0
    for i in p:
        for j in range(N-1):
            ans += math.sqrt((xy[i[j]][0]-xy[i[j+1]][0])**2 + (xy[i[j]][1]-xy[i[j+1]][1])**2)
    print(ans/math.factorial(N))
