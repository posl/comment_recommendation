def main():
    n = int(input())
    a = list(map(int, input().split()))
    res = [0] * (2 * n + 1)
    for i in range(n):
        res[a[i]] = i + 1
    for i in range(1, 2 * n + 1):
        print(res[i])
