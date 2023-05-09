def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    Asum = [0]
    Bsum = [0]
    for i in range(N):
        Asum.append(Asum[i] + A[i])
        Bsum.append(Bsum[i] + B[i])
    ans = N
    for i in range(N):
        if A[i] > B[i]:
            ans = i
            break
    for i in range(N):
        if B[i] > A[N-1-i]:
            ans = min(ans, i)
            break
    for i in range(N):
        if A[i] > B[N-1-i]:
            ans = min(ans, i)
            break
    for i in range(N):
        if B[i] > A[N-1-i]:
            ans = min(ans, i)
            break
    for i in range(N):
        if A[i] > B[N-1-i]:
            ans = min(ans, i)
            break
    print(ans)
