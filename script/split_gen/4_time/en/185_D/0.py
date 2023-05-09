def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if M == 0:
        print(1)
        return
    if N == M:
        print(0)
        return
    diff = []
    for i in range(M):
        if i == 0:
            diff.append(A[i] - 1)
        else:
            diff.append(A[i] - A[i - 1] - 1)
    diff.append(N - A[M - 1])
    diff.sort()
    diff.reverse()
    k = diff[0]
    count = 0
    for i in range(M + 1):
        count += (diff[i] + k - 1) // k
    print(count)
