def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    b = []
    for i in range(n):
        b.append(abs(t - h[i] * 0.006 - a))
    print(b.index(min(b)) + 1)
