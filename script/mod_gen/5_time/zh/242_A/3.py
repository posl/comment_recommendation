def main():
    A, B, C, X = map(int, input().split())
    print(C/(B-A) if A <= X <= B else 0)

if __name__ == '__main__':
    main()