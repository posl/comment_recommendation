def main():
    N, M = map(int, input().split())
    food = [0] * M
    for i in range(N):
        A = list(map(int, input().split()))
        for j in range(A[0]):
            food[A[j+1]-1] += 1
    count = 0
    for i in range(M):
        if food[i] == N:
            count += 1
    print(count)
