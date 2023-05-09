def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = {}
    for i in range(n):
        if a[i] in b:
            b[a[i]] += 1
        else:
            b[a[i]] = 1
    ans = [0] * n
    for i in range(n):
        ans[i] = n - b.get(a[i]) + 1
    print('\n'.join(map(str, ans)))
