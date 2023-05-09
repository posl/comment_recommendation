def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    total = 10**9
    for i in range(n - k + 1):
        left = x[i]
        right = x[i + k - 1]
        if left < 0 and right < 0:
            total = min(total, -left)
        elif left < 0 and right >= 0:
            total = min(total, -left + right + min(-left, right))
        else:
            total = min(total, right)
    print(total)
