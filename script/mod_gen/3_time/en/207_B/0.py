def main():
    A, B, C, D = map(int, input().split())
    if A > B * D:
        print(-1)
        return
    if C <= D * B:
        print(1)
        return
    print((A - B * D - 1) // (C - D * B) + 2)
main()
