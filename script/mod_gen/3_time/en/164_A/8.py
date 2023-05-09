def main():
    s, w = map(int, input().split())
    print("safe" if s > w else "unsafe")

if __name__ == '__main__':
    main()