def main():
    a,b,c = map(int,input().split())
    if a == b and b == c:
        print("No")
    elif a == b or a == c or b == c:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()