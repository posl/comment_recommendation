def solve():
    A,B,N = map(int, input().split())
    ans = 0
    if B > N:
        ans = min(A-1, N)
    else:
        ans = min(A-1, B-1)
        ans = ans * (N // B)
        ans += (N % B) // A
    print(ans)
