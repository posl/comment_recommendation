def main():
    S, T = input().rstrip().split()
    A, B = map(int, input().rstrip().split())
    U = input().rstrip()
    if U == S:
        A -= 1
    else:
        B -= 1
    print(A, B)

if __name__ == '__main__':
    main()