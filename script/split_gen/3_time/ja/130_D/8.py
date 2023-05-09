def main():
    N,K = map(int,input().split())
    a = list(map(int,input().split()))
    s = 0
    left = 0
    right = 0
    ans = 0
    while right < N:
        while s < K:
            if right == N:
                break
            s += a[right]
            right += 1
        while s >= K:
            ans += N - right + 1
            s -= a[left]
            left += 1
    print(ans)
