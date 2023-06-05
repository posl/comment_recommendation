def main():
    x, y, z = map(int, input().split())
    print(x + z if x < y < z else -1)

if __name__ == '__main__':
    main()