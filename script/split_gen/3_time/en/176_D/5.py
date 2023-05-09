def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    C_h -= 1
    C_w -= 1
    D_h, D_w = map(int, input().split())
    D_h -= 1
    D_w -= 1
    S = []
    for h in range(H):
        S.append(list(input()))
    Q = []
    Q.append([C_h, C_w, 0])
    S[C_h][C_w] = 1
    while len(Q) > 0:
        h, w, c = Q.pop(0)
        if h == D_h and w == D_w:
            print(c)
            return
        for dh, dw in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            if 0 <= h + dh < H and 0 <= w + dw < W and S[h + dh][w + dw] == ".":
                S[h + dh][w + dw] = c + 1
                Q.append([h + dh, w + dw, c + 1])
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                if 0 <= h + dh < H and 0 <= w + dw < W and S[h + dh][w + dw] == ".":
                    S[h + dh][w + dw] = c + 1
                    Q.append([h + dh, w + dw, c + 1])
    print(-1)
    return
main()
I wrote a solution in python3. It is easy to understand, but it is not efficient. It is O(HW) in time complexity.
I think this problem is a kind of BFS.
I think this problem is a kind of BFS.
Yes, it is.
Thanks for your answer. I think I should try to use BFS in the future.
