def main():
    a, b = map(int, input().split())
    if (a + b) % 2 == 0:
        print(int((a + b) / 2))
    else:
        print("IMPOSSIBLE")

if __name__ == '__main__':
    main()