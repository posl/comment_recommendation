def main():
    A,B,C = map(int, input().split())
    if A == B:
        print("=")
    elif C % 2 == 0:
        A = abs(A)
        B = abs(B)
        if A > B:
            print(">")
        else:
            print("<")
    elif C % 2 != 0:
        if A > B:
            print(">")
        else:
            print("<")
