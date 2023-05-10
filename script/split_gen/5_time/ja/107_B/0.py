def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    rows = [False] * H
    columns = [False] * W
    for i in range(H):
        for j in range(W):
            if a[i][j] == "#":
                rows[i] = True
                columns[j] = True
    for i in range(H):
        if rows[i]:
            for j in range(W):
                if columns[j]:
                    print(a[i][j], end="")
            print()
