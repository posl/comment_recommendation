def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 0
    right = 0
    total = 0
    for left in range(N):
        while right < N and total < K:
            total += A[right]
            right += 1
        if total < K:
            break
        ans += N - right + 1
        if right == left:
            right += 1
        else:
            total -= A[left]
    print(ans)
