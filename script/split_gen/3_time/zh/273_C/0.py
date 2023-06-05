def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    n = len(a)
    ans = [0] * n
    for i in range(n):
        ans[i] = i
    for i in range(1, n):
        if a[i] == a[i-1]:
            ans[i] = ans[i-1]
    for i in range(n-2, -1, -1):
        if a[i] == a[i+1]:
            ans[i] = ans[i+1]
    for i in range(n):
        print(ans[i])
