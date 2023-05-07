def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min = A
    if B < min:
        min = B
    if C < min:
        min = C
    if D < min:
        min = D
    if E < min:
        min = E
    print((N + min - 1) // min + 4)

if __name__ == '__main__':
    main()