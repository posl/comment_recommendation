def main():
    N, M = map(int, input().split())
    A = [0] * M
    for i in range(N):
        K, *tmp = map(int, input().split())
        for j in tmp:
            A[j-1] += 1
    print(A.count(N))
