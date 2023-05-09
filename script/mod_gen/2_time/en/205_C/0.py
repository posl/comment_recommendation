def main():
    A, B, C = map(int, input().split())
    if pow(A, C) > pow(B, C):
        print(">")
    elif pow(A, C) < pow(B, C):
        print("<")
    else:
        print("=")

if __name__ == '__main__':
    main()