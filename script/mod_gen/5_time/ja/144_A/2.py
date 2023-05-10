def main():
    A, B = map(int, input().split())
    if 0 < A <= 20 and 0 < B <= 20:
        print(A * B if A * B <= 20 else -1)
    else:
        print(-1)

if __name__ == '__main__':
    main()