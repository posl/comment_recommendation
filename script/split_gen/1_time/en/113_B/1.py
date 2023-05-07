def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i == 0:
            ans = abs(t - h[i] * 0.006 - a)
        else:
            if abs(t - h[i] * 0.006 - a) < ans:
                ans = abs(t - h[i] * 0.006 - a)
                index = i
    print(index + 1)
