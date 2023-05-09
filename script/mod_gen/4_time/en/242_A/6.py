def main():
    A, B, C, X = map(int, input().split())
    print((A <= X and X <= B) * C / (B - A + 1))

if __name__ == '__main__':
    main()