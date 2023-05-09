def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    a.sort()
    for i in range(q):
        ans = n
        left = 0
        right = n-1
        while left <= right:
            mid = (left + right) // 2
            if a[mid] < x[i]:
                left = mid + 1
            else:
                right = mid - 1
                ans = mid
        print(n-ans)
