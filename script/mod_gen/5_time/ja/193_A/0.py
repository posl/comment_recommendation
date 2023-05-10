def main():
    a, b = map(int, input().split())
    print(100 - ((b / a) * 100))

if __name__ == '__main__':
    main()