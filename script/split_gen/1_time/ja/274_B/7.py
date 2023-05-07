def main():
    H, W = map(int, input().split())
    X = [0] * W
    for _ in range(H):
        for j, C in enumerate(input()):
            if C == "#":
                X[j] += 1
    print(*X)
