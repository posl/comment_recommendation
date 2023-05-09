def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    s = 0
    for i in range(n):
        if a[i] <= s + 1:
            s += a[i]
    print(s + 1)
