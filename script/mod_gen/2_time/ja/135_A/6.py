def main():
    a, b = map(int, input().split())
    if (b - a) % 2 == 0:
        print((b + a) // 2)
    else:
        print("IMPOSSIBLE")

if __name__ == '__main__':
    main()