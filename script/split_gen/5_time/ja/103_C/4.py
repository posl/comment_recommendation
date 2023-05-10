def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    ans = 0
    for i in range(a[0]):
        tmp = 0
        for j in range(n):
            tmp += i % a[j]
        ans = max(ans, tmp)
    print(ans)
