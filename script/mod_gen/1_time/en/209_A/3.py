def main():
    A, B = map(int, input().split())
    print(max(0, B - A + 1))

if __name__ == '__main__':
    main()