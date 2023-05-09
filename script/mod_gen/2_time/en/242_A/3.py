def main():
    A, B, C, X = map(int, input().split())
    if X < A:
        print(0)
    elif X >= A and X <= B:
        print(1/C)
    else:
        print(1)

if __name__ == '__main__':
    main()