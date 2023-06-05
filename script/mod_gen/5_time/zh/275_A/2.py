def main():
    n = int(input())
    height = list(map(int, input().split()))
    print(height.index(max(height)) + 1)

if __name__ == '__main__':
    main()