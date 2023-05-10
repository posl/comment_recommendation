def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    diff = float('inf')
    for i in range(n):
        tmp = abs(a - (t - h[i] * 0.006))
        if diff > tmp:
            ans = i + 1
            diff = tmp
    print(ans)
