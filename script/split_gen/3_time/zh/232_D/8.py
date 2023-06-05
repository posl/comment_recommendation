def main():
    H, W = map(int, input().split())
    c = [input() for _ in range(H)]
    print(H, W)
    print(c)
    print(c[0][1])
    print(c[1][0])
    print(c[0][0])
    # for i in range(H):
    #     for j in range(W):
    #         print(c[i][j])
