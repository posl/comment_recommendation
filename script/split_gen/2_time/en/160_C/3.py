def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0] + K)
    d = [A[i + 1] - A[i] for i in range(N)]
    print(sum(d) - max(d))
