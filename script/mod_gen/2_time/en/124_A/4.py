def main():
    A, B = map(int, input().split())
    if A == B:
        print(A * 2)
    else:
        print(max(A, B) * 2 - 1)

if __name__ == '__main__':
    main()