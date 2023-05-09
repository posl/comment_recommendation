def main():
    A, B, C, D = map(int, input().split())
    if A <= B * D:
        print(-1)
    else:
        print((A + C - B - 1) // (C - B))
