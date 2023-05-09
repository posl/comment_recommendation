def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n - 1):
        if a[i] * 2 < a[i + 1]:
            a[i + 1] = a[i]
    print(a.count(a[-1]))
