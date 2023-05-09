def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N+1):
        left = bisect_left(A, i)
        right = bisect_right(A, i)
        ans += (right - left) * (right - left - 1) // 2
    print(ans)
