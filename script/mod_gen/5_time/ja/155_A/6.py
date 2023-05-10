def main():
    a,b,c = map(int,input().split())
    if a == b:
        if a == c:
            print("No")
        else:
            print("Yes")
    elif b == c:
        print("Yes")
    elif a == c:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()