def main():
    N = int(input())
    p = list(map(int, input().split()))
    # 从左到右，从右到左的最大连续数
    left = [0] * N
    right = [0] * N
    # 从左到右，从右到左的最大连续数
    for i in range(N-1):
        if p[i] < p[i+1]:
            left[i+1] = left[i] + 1
    for i in range(N-1, 0, -1):
        if p[i-1] < p[i]:
            right[i-1] = right[i] + 1
    # 从左到右，从右到左的最大连续数
    for i in range(N):
        if p[i] < p[(i+1)%N]:
            left[i] = left[(i+1)%N] + 1
    for i in range(N-1, -1, -1):
        if p[i] < p[(i-1)%N]:
            right[i] = right[(i-1)%N] + 1
    ans = 0
    for i in range(N):
        ans = max(ans, left[i]+right[i]+1)
    print(ans)
