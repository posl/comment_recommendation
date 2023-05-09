def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    h = [t - i * 0.006 for i in h]
    ans = 0
    ans_temp = 1000000000
    for i in range(n):
        if ans_temp > abs(a - h[i]):
            ans_temp = abs(a - h[i])
            ans = i + 1
    print(ans)
