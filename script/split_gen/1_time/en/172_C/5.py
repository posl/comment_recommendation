def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    i = 0
    j = 0
    time = 0
    while i < N and time + A[i] <= K:
        time += A[i]
        i += 1
    ans = i
    while j < M and i >= 0:
        time += B[j]
        j += 1
        while time > K and i > 0:
            i -= 1
            time -= A[i]
        if time <= K:
            ans = max(ans, i + j)
    print(ans)
