def main():
    a,b,c,d,e = map(int,input().split())
    if a == b and c == d and d == e:
        print("Yes")
    elif a == c and b == d and d == e:
        print("Yes")
    elif a == d and b == c and c == e:
        print("Yes")
    elif a == e and b == c and c == d:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()