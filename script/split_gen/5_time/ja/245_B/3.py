def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if ans < a[i]:
            print(ans)
            break
        ans += a[i]
