def main():
    A, B, C = map(int, input().split())
    pow_A = A ** C
    pow_B = B ** C
    if pow_A > pow_B:
        print(">")
    elif pow_A == pow_B:
        print("=")
    else:
        print("<")

if __name__ == '__main__':
    main()