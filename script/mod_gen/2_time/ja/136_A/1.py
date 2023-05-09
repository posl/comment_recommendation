def main():
    A, B, C = map(int, input().split())
    if A - B < C:
        print(A - B)
    else:
        print(C)

if __name__ == '__main__':
    main()