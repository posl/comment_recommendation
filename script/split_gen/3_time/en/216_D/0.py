def main():
    N, M = map(int, input().split())
    K = []
    A = []
    for _ in range(M):
        k = int(input())
        a = list(map(int, input().split()))
        K.append(k)
        A.append(a)
    print("Yes" if solve(N, M, K, A) else "No")
