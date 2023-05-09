def main():
    A, B, C, D = map(int, input().split())
    if A <= B * D:
        print(0)
        return
    if C <= B:
        print(-1)
        return
    print((A - B * D + B * C - B - 1) // (B * C - B) + 1)

if __name__ == '__main__':
    main()