def main():
    A, B, C, D = map(int, input().split())
    if A <= B * D:
        print(-1)
    else:
        print((A + B - C - 1) // (B - C))

if __name__ == '__main__':
    main()