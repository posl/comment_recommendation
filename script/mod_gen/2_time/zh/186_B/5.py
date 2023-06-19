def solve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    min_A = min(map(min, A))
    print(sum(map(lambda x: sum(map(lambda y: y - min_A, x)), A)))

if __name__ == '__main__':
    solve()