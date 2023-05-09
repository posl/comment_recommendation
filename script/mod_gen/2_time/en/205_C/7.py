def main():
    # Read the input
    A, B, C = map(int, input().split())
    # Display the result
    if pow(A, C) > pow(B, C):
        print(">")
    elif pow(A, C) < pow(B, C):
        print("<")
    else:
        print("=")

if __name__ == '__main__':
    main()