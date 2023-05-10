def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] > 1:
        print(0)
    else:
        ans = 1
        for i in range(1, N):
            if a[i] > ans * 2:
                break
            else:
                ans += a[i]
        print(ans)
