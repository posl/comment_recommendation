def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A + [N+1]
    B = []
    for i in range(M+1):
        B.append(A[i+1] - A[i] - 1)
    B.sort()
    B = B[::-1]
    ans = 0
    for i in range(M+1):
        if i < N % (M+1):
            ans += B[i]//(N//(M+1)+1)
        else:
            ans += B[i]//(N//(M+1))
    print(ans)
