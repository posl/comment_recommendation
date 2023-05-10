def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    min = 100000
    ans = 0
    for i in range(n):
        if min > abs(a - (t - h[i] * 0.006)):
            min = abs(a - (t - h[i] * 0.006))
            ans = i + 1
    print(ans)
