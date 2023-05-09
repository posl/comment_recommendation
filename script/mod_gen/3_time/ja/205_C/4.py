def main():
    A,B,C = map(int,input().split())
    if A == B:
        print("=")
    elif C % 2 == 0:
        if abs(A) == abs(B):
            print("=")
        elif abs(A) > abs(B):
            print(">")
        else:
            print("<")
    elif C % 2 == 1:
        if A > B:
            print(">")
        else:
            print("<")

if __name__ == '__main__':
    main()