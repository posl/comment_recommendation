def main():
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    s = 0
    for i in range(n):
        s += (b[i] - a[i] + 1) * (b[i] + a[i]) // 2
    print(s % 1000000007)
    return
