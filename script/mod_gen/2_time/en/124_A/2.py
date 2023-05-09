def main():
    A, B = map(int, input().split())
    print(max(2 * A - 1, 2 * B - 1, A + B))

if __name__ == '__main__':
    main()