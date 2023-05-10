def main():
    # input
    A, B, C, D = map(int, input().split())
    # compute
    if A > B * D:
        result = -1
    else:
        result = (C * A - 1) // (B * D - A) + 1
    # output
    print(result)
