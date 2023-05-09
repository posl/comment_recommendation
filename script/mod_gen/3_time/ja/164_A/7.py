def main():
    sheep, wolf = map(int, input().split())
    print("safe" if sheep > wolf else "unsafe")

if __name__ == '__main__':
    main()