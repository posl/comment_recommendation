def main():
    n, w = map(int, input().split())
    a = [0] * 200001
    for _ in range(n):
        s, t, p = map(int, input().split())
        a[s] += p
        a[t] -= p
    for i in range(1, 200001):
        a[i] += a[i - 1]
    if max(a) <= w:
        print("Yes")
    else:
        print("No")
