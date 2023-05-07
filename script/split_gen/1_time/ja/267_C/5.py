def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    print(sum((i+1)*A[i] for i in range(M)))
