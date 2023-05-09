def main():
    R, C = map(int, input().split())
    print("black" if (R + C) % 2 == 0 else "white")

if __name__ == '__main__':
    main()