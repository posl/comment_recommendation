def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    a = [0] + a
    for i in range(1, n+1):
        a[i] += a[i-1]
    t %= a[-1]
    for i in range(1, n+1):
        if a[i] > t:
            print(i, t-a[i-1])
            break
