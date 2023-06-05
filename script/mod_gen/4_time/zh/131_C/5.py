def main():
    A,B,C,D = map(int, input().split())
    a = A // C
    b = B // C
    c = A // D
    d = B // D
    e = A // (C * D)
    f = B // (C * D)
    if A % C == 0:
        a -= 1
    if A % D == 0:
        c -= 1
    if A % (C * D) == 0:
        e -= 1
    print(B - A + 1 - (b - a) - (d - c) + (f - e))

if __name__ == '__main__':
    main()