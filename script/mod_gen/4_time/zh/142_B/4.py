def main():
    num, height = map(int, input().split())
    heights = list(map(int, input().split()))
    count = 0
    for h in heights:
        if h >= height:
            count += 1
    print(count)

if __name__ == '__main__':
    main()