def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % M for a in A]
    A = [0] + A
    for i in range(1, N+1):
        A[i] = (A[i-1] + A[i]) % M
    A.sort()
    count = 0
    prev = A[0]
    cnt = 1
    for i in range(1, N+1):
        if A[i] == prev:
            cnt += 1
        else:
            count += (cnt * (cnt-1)) // 2
            prev = A[i]
            cnt = 1
    count += (cnt * (cnt-1)) // 2
    print(count)
