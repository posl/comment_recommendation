def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (2 * N + 1)
    for i in range(N):
        B[A[i]] = i + 1
    from collections import deque
    Q = deque()
    Q.append((1, 0))
    while Q:
        i, d = Q.popleft()
        print(d)
        if 2 * i <= 2 * N and B[2 * i] != 0:
            Q.append((2 * i, d + 1))
        if 2 * i + 1 <= 2 * N and B[2 * i + 1] != 0:
            Q.append((2 * i + 1, d + 1))
