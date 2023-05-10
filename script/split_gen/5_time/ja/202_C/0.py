def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort()
    B.sort()
    C.sort()
    ans = 0
    a = 0
    c = 0
    for b in range(n):
        while a < n and A[a] < B[b]:
            a += 1
        while c < n and C[c] <= B[b]:
            c += 1
        ans += a * (n - c)
    print(ans)
