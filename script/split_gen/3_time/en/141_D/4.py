def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    sum = 0
    for i in range(0, N):
        sum += A[i]
    for i in range(0, M):
        sum = sum // 2
    print(sum)
