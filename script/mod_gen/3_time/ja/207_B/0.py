def main():
    A, B, C, D = map(int, input().split())
    if A <= B * D:
        print(0)
    elif C <= B * D:
        print(-1)
    else:
        print((A - B * D + C - B * D - 1) // (C - B * D) + 1)

if __name__ == '__main__':
    main()