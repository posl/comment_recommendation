def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    min_t = float('inf')
    for i in range(n):
        tmp = t - h[i] * 0.006
        if abs(tmp - a) < min_t:
            min_t = abs(tmp - a)
            ans = i + 1
    print(ans)
