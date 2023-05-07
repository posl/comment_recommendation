def main():
    A, B, C, D = map(int, input().split())
    while A > 0 and C > 0:
        C -= B
        A -= D
    print("Yes" if A > 0 else "No")

if __name__ == '__main__':
    main()