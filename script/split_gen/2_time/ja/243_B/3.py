def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i] = A[i]
        b[i] = B[i]
    a.sort()
    b.sort()
    i = 0
    j = 0
    cnt = 0
    while i < N and j < N:
        if a[i] == b[j]:
            cnt += 1
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    print(cnt)
    print(N - cnt)
