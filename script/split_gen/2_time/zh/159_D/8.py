def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(0)
    cnt = 0
    ans = 0
    for i in range(n):
        if a[i] == a[i+1]:
            cnt += 1
        else:
            ans += cnt * (cnt + 1) // 2
            cnt = 0
    for i in range(n):
        print(ans)
        ans += 1
        if i == n - 1 or a[i] != a[i+1]:
            ans -= 1
    return
