def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 1
    for i in range(n):
        if a[i] > ans:
            break
        else:
            ans += a[i]
    print(ans)
