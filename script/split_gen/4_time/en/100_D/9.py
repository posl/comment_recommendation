def main():
    n, m = map(int, input().split())
    cakes = [list(map(int, input().split())) for i in range(n)]
    # 0: -x, 1: +x
    # 0: -y, 1: +y
    # 0: -z, 1: +z
    signs = [[0, 1] for i in range(8)]
    ans = 0
    for i in range(8):
        cakes.sort(key=lambda x: (x[0] * signs[i][0] + x[1] * signs[i][1] + x[2] * signs[i][2]), reverse=True)
        ans = max(ans, sum(map(lambda x: x[0] * signs[i][0] + x[1] * signs[i][1] + x[2] * signs[i][2], cakes[:m])))
    print(ans)
