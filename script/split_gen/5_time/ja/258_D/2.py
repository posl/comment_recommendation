def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    min_time = float('inf')
    for i in range(N):
        time = A[i]
        cnt = 1
        for j in range(N):
            if i == j:
                continue
            time += B[j]
            cnt += 1
            if cnt >= X:
                break
        min_time = min(min_time, time)
    print(min_time)
