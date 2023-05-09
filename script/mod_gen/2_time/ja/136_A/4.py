def main():
    A, B, C = map(int, input().split())
    if B+C >= A:
        print(B+C-A)
    else:
        print(0)

if __name__ == '__main__':
    main()