def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [0] * q
    for i in range(q):
        x[i] = int(input())
    a.sort()
    for i in range(q):
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            if a[mid] < x[i]:
                left = mid + 1
            else:
                right = mid
        if a[left] < x[i]:
            print(n - left)
        else:
            print(n - left - 1)
