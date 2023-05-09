def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] != 1:
        print(0)
    else:
        ans = 1
        for i in range(1, N):
            if ans + 1 == a[i]:
                ans += 1
            elif ans + 1 < a[i]:
                break
        print(ans)
