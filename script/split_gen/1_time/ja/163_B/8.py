def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(M):
        N -= A[i]
    print(N)
