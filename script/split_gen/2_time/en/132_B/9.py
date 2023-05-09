def main():
    n = int(input())
    p = list(map(int, input().split()))
    # p[i]がp[i-1], p[i], p[i+1]の中で2番目に小さい値であるかどうかを判定する
    # 2番目に小さい値を求めるには、3つの値のうち最大値と最小値を求めればよい
    ans = 0
    for i in range(1, n - 1):
        if p[i] > max(p[i - 1], p[i + 1]) or p[i] < min(p[i - 1], p[i + 1]):
            continue
        ans += 1
    print(ans)
