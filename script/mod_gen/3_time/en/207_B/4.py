def main():
    A, B, C, D = map(int, input().split())
    if B > C * D:
        print(-1)
        return
    if A <= B:
        print(0)
        return
    if C <= D:
        print(-1)
        return
    print((A - B + B * D - 1) // (B * D - C * D) + 1)

if __name__ == '__main__':
    main()