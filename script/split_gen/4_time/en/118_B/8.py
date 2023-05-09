def main():
    N, M = map(int, input().split())
    A = [0]*M
    for i in range(N):
        K, *a = map(int, input().split())
        for j in a:
            A[j-1] += 1
    print(A.count(N))
