def main():
    A, B = map(int, input().split())
    if A == B:
        print(A + B)
    else:
        print(max(A, B) + max(A, B) - 1)

if __name__ == '__main__':
    main()