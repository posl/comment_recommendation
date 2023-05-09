def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(N):
        if i == 0:
            ans += 1
        elif a[i-1] != a[i]:
            ans += 1
    print(ans)
