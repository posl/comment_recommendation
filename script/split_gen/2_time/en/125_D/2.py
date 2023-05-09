def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += abs(A[i])
    if N % 2 == 0:
        print(ans)
    else:
        print(ans - 2 * min([abs(a) for a in A]))
