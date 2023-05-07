def main():
    A, B, C, D = map(int, input().split())
    if D * C < B:
        print(-1)
        return
    if A <= B * D:
        print(0)
        return
    print((A - B * D + B * C - 1) // (B * C - B * D))
