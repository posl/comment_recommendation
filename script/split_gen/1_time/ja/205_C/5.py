def main():
    A, B, C = map(int, input().split())
    if A < 0 and B > 0:
        if C % 2 == 0:
            if A ** C > B ** C:
                print(">")
            elif A ** C < B ** C:
                print("<")
            else:
                print("=")
        else:
            if A ** C > B ** C:
                print("<")
            elif A ** C < B ** C:
                print(">")
            else:
                print("=")
    else:
        if A ** C > B ** C:
            print(">")
        elif A ** C < B ** C:
            print("<")
        else:
            print("=")
