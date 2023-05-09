def main():
    r, c = map(int, input().split())
    print("black" if (r + c) % 2 == 0 else "white")

if __name__ == '__main__':
    main()