def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if ans + 1 == a[i]:
            ans += 1
    print(ans)
