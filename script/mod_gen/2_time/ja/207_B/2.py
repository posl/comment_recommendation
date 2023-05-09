def main():
    A, B, C, D = map(int, input().split())
    if A > B * D:
        print(-1)
    else:
        print((B * D - A + C - 1) // C)

if __name__ == '__main__':
    main()