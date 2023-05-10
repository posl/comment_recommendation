def main():
    N,M = map(int,input().split())
    if M == 0:
        print(1)
        return
    A = list(map(int,input().split()))
    A.sort()
    if A[0] != 1:
        A.insert(0,0)
    if A[-1] != N:
        A.append(N+1)
    k = N
    for i in range(len(A)-1):
        if A[i+1] - A[i] - 1 != 0:
            k = min(k,A[i+1] - A[i] - 1)
    ans = 0
    for i in range(len(A)-1):
        if A[i+1] - A[i] - 1 != 0:
            ans += (A[i+1] - A[i] - 1 + k - 1) // k
    print(ans)
