def main():
    A, B, K = map(int, input().split())
    if A >= B:
        print(0)
    else:
        print(min(B - A, K))

if __name__ == '__main__':
    main()