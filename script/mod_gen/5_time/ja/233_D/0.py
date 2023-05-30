def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    right = 0
    now = 0
    for left in range(n):
        while right < n and now < k:
            now += a[right]
            right += 1
        if now == k:
            ans += 1
        if right == left:
            right += 1
        else:
            now -= a[left]
    print(ans)
main()
