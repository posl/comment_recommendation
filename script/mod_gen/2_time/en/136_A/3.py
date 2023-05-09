def main():
    A, B, C = map(int, input().split())
    print(max(C - (A - B), 0))

if __name__ == '__main__':
    main()