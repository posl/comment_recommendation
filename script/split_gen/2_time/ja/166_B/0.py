def main():
    N, K = map(int, input().split())
    d = [0] * K
    A = [0] * K
    for i in range(K):
        d[i] = int(input())
        A[i] = list(map(int, input().split()))
    ans = N
    for i in range(K):
        ans -= len(A[i])
    print(ans)
