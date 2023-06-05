def main():
    S, T = raw_input().split()
    A, B = map(int, raw_input().split())
    U = raw_input()
    if U == S:
        A -= 1
    else:
        B -= 1
    print A, B

if __name__ == '__main__':
    main()