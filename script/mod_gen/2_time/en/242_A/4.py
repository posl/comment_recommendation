def main():
    A, B, C, X = map(int, input().split())
    print(((C / (B - A + 1)) if A <= X <= B else 0) + (1 if X <= A else 0))

if __name__ == '__main__':
    main()