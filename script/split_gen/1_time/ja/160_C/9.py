def main():
    # 標準入力から整数を取得する
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    a.append(a[0]+k)
    max = 0
    for i in range(1, n+1):
        if a[i] - a[i-1] > max:
            max = a[i] - a[i-1]
    print(k - max)
