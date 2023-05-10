def main():
    N, A, B = map(int, input().split())
    if A > B:
        print(0)
    elif A == B:
        print(1)
    elif N == 1:
        print(1)
    else:
        print((N-2)*(B-A)+1)

if __name__ == '__main__':
    main()