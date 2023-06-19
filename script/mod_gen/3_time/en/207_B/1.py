def main():
    A, B, C, D = map(int, input().split())
    if A > B * D:
        print(-1)
        return
    if C >= B:
        print(-1)
        return
    if C <= D:
        print(-1)
        return
    if A <= B * C:
        print(1)
        return
    if A > B * C:
        print(1 + (A - B * C - 1) // ((B - C) * D))
        return
main()
