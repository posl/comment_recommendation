def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a%M for a in A]
    A = [0] + A
    for i in range(1, N+1):
        A[i] = (A[i-1] + A[i])%M
    from collections import Counter
    c = Counter(A)
    ans = 0
    for k in c:
        ans += c[k]*(c[k]-1)//2
    print(ans)
