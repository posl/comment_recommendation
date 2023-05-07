def solve():
    N, M = map(int, input().split())
    A = [list(map(int, input().split()))[1:] for _ in range(M)]
    for i in range(N):
        for j in range(i+1, N):
            if not any([i+1 in a and j+1 in a for a in A]):
                return False
    return True
print('Yes' if solve() else 'No')

if __name__ == '__main__':
    solve()