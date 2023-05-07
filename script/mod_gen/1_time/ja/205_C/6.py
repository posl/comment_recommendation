def main():
    A,B,C=map(int,input().split())
    if A<0 and C%2==1:
        if A**C > B**C:
            print(">")
        elif A**C < B**C:
            print("<")
        else:
            print("=")
    else:
        if A**C > B**C:
            print(">")
        elif A**C < B**C:
            print("<")
        else:
            print("=")

if __name__ == '__main__':
    main()