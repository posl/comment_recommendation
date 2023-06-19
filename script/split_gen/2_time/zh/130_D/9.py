def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = 0
    res = 0
    right = 0
    for left in range(n):
        while right < n and s < k:
            s += a[right]
            right += 1
        if s < k:
            break
        res += n - right + 1
        s -= a[left]
    print(res)
