def main():
    n, l = map(int, input().split())
    s = 0
    for i in range(1, n+1):
        s += l + i - 1
    if s > 0:
        print(s - l)
    else:
        print(s - l + n - 1)
