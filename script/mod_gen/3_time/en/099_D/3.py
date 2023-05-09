def main():
    N, C = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(C)]
    c = [list(map(int, input().split())) for _ in range(N)]
    def cost(x, y):
        return D[(x + y) % 3][y]
    res = 0
    for i in range(3):
        res += sum(cost(c[j][k] - 1, i) for j in range(N) for k in range(N))
    print(res)

if __name__ == '__main__':
    main()