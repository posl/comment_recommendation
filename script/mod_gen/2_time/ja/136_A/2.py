def main():
    A, B, C = map(int, input().split())
    if B + C <= A:
        print(0)
    else:
        print(B + C - A)

if __name__ == '__main__':
    main()