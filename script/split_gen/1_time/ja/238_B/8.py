def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(n)
    #print(a)
    #最大の角度を求める
    max = 0
    for i in range(n):
        if max < a[i]:
            max = a[i]
    #print(max)
    #最大の角度との差が最小の角度を求める
    min = 360
    for i in range(n):
        if min > abs(max - a[i]):
            min = abs(max - a[i])
    print(360 - min)
