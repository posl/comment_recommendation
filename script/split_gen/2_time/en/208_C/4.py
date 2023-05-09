def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A
    for i in range(1, N+1):
        A[i] -= i
    A.append(10**10)
    L = 0
    R = 10**9
    while R-L > 1:
        M = (L+R)//2
        if A[M] <= K:
            L = M
        else:
            R = M
    for i in range(1, N+1):
        if A[i] <= K:
            print(K//L)
        else:
            print(K//L + 1)
