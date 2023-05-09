def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(K + A[0])
    D = [A[i + 1] - A[i] for i in range(N)]
    print(K - max(D))
