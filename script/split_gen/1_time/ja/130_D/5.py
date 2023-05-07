def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    count = 0
    sum = 0
    for i in range(N):
        sum += A[i]
        if sum >= K:
            count += 1
        else:
            ans += count
            count = 0
            sum = 0
    ans += count * (count + 1) // 2
    print(ans)
