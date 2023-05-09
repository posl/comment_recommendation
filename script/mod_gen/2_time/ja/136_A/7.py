def main():
    A, B, C = map(int, input().split())
    print(max(0, min(C, B + C - A)))

if __name__ == '__main__':
    main()