def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    
    B_count = [0] * N
    for b in B:
        B_count[b - 1] += 1
    C_count = [0] * N
    for c in C:
        C_count[c - 1] += 1
    ans = 0
    for a in A:
        ans += B_count[a - 1] * C_count[a - 1]
    return ans

if __name__ == '__main__':
    solve()