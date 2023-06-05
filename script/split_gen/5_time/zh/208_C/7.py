def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a = a[::-1]
    ans = [k//n for i in range(n)]
    k = k%n
    for i in range(k):
        ans[i] += 1
    for i in range(n):
        print(ans[a.index(a[i])])
