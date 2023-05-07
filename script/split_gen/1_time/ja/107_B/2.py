def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    for i in range(H):
        if "#" in a[i]:
            continue
        a[i] = ""
    for j in range(W):
        if "#" in [a[i][j] for i in range(H)]:
            continue
        for i in range(H):
            a[i] = a[i][:j] + a[i][j+1:]
    for i in range(H):
        print(a[i])
