def main():
    A, B, C = [int(x) for x in input().split()]
    if A == B:
        print("=")
    elif A < 0 and B < 0:
        if C % 2 == 0:
            if A < B:
                print(">")
            else:
                print("<")
        else:
            if A < B:
                print("<")
            else:
                print(">")
    elif A < 0:
        if C % 2 == 0:
            if A < B:
                print(">")
            else:
                print("<")
        else:
            print("<")
    elif B < 0:
        if C % 2 == 0:
            if A < B:
                print(">")
            else:
                print("<")
        else:
            print(">")
    else:
        if A < B:
            print("<")
        else:
            print(">")
