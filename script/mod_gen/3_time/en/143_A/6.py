def main():
    A, B = map(int, input().split())
    print(max(0, A - B * 2))

if __name__ == '__main__':
    main()