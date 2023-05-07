def main():
    A, B, C, D = map(int, input().split())
    if A <= B * D:
        print(-1)
        return
    if C * D <= B:
        print(0)
        return
    if A <= B * C:
        print(1)
        return
    print((A - B * C + (C * D - B) - 1) // (C * D - B) + 1)
