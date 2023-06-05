def main():
    S, T = input().split()
    A, B = map(int, input().split())
    U = input()
    if U == S:
        A -= 1
    elif U == T:
        B -= 1
    print(A, B)

if __name__ == '__main__':
    main()