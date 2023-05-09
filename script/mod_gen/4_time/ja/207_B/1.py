def main():
    A, B, C, D = map(int, input().split())
    if A <= B * D:
        print(-1)
        return
    if B <= C * D:
        print(0)
        return
    if B > C * D:
        print((A - 1) // (B - C * D) + 1)
        return

if __name__ == '__main__':
    main()