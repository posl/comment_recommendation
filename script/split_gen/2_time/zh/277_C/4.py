def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    if N == 1:
        print(max(A[0], B[0]))
        exit()
    A.sort()
    B.sort()
    if N % 2 == 0:
        l = N // 2
        r = l + 1
        ans = (B[l - 1] + B[r - 1]) - (A[l - 1] + A[r - 1]) + 1
    else:
        l = N // 2 + 1
        ans = B[l - 1] - A[l - 1] + 1
    print(ans)
