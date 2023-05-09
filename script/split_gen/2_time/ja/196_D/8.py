def main():
    H, W, A, B = map(int, input().split())
    print(H * W - (2 * A + B))
