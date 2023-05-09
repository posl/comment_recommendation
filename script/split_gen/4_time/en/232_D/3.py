def main():
    H, W = map(int, input().split())
    C = []
    for _ in range(H):
        C.append(list(input()))
    count = 1
    i = 0
    j = 0
    while True:
        if i == H - 1 and j == W - 1:
            break
        if i < H - 1 and C[i + 1][j] == ".":
            i += 1
            count += 1
            continue
        if j < W - 1 and C[i][j + 1] == ".":
            j += 1
            count += 1
            continue
        break
    print(count)
