def main():
    n = int(input())
    s = list(map(int, input().split()))
    a = [0 for _ in range(n)]
    a[0] = s[0]
    for i in range(1, n):
        a[i] = s[i] - s[i-1]
    print(*a)
