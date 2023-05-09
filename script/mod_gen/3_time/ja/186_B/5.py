def solve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    min_A = min([min(a) for a in A])
    print(sum([sum(a) - min_A * W for a in A]))

if __name__ == '__main__':
    solve()