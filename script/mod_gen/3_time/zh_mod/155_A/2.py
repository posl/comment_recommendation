def main():
    a,b,c = map(int,input().split())
    if a==b and b!=c:
        print("Yes")
    elif a==c and b!=c:
        print("Yes")
    elif b==c and a!=c:
        print("Yes")
    else:

if __name__ == '__main__':
    main()