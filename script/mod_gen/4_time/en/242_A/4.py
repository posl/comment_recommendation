def main():
    A, B, C, X = map(int, input().split())
    print(1 - (B - X) / (B - A) if A <= X <= B else 0)
main()

if __name__ == '__main__':
    main()