def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for x in range(1, 10**5+1):
        left = 0
        right = 0
        while left < N:
            while right < N and A[right] >= x:
                right += 1
            ans = max(ans, x*(right-left))
            left = right
            while left < N and A[left] < x:
                left += 1
            right = left
    print(ans)
