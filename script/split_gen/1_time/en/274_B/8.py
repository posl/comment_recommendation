def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    for j in range(W):
        print(sum(c[j] == '#' for c in C))
