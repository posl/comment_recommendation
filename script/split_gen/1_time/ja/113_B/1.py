def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    for i in range(n):
        h[i] = abs(a - t + h[i] * 0.006)
    print(h.index(min(h)) + 1)
