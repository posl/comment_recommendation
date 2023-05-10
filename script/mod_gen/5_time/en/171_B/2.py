def solve(N, K, p):
    p.sort()
    return sum(p[:K])
N, K = map(int, input().split())
p = list(map(int, input().split()))
print(solve(N, K, p))

if __name__ == '__main__':
    solve()