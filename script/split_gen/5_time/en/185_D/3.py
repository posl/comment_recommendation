def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if M == 0:
        print(1)
        return
    A.sort()
    if A[0] != 1:
        A.insert(0, 0)
    if A[-1] != N:
        A.append(N+1)
    max_k = 0
    for i in range(1, len(A)):
        k = A[i] - A[i-1] - 1
        if k > max_k:
            max_k = k
    ans = 0
    for i in range(1, len(A)):
        k = A[i] - A[i-1] - 1
        if k == max_k:
            ans += 1
    print(ans)
