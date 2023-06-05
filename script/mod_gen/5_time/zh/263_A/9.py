def main():
    a,b,c,d,e = map(int,input().split())
    if a == b and a == c and a != d and a != e:
        print("Yes")
    elif a == b and a == d and a != c and a != e:
        print("Yes")
    elif a == b and a == e and a != c and a != d:
        print("Yes")
    elif a == c and a == d and a != b and a != e:
        print("Yes")
    elif a == c and a == e and a != b and a != d:
        print("Yes")
    elif a == d and a == e and a != b and a != c:
        print("Yes")
    elif b == c and b == d and b != a and b != e:
        print("Yes")
    elif b == c and b == e and b != a and b != d:
        print("Yes")
    elif b == d and b == e and b != a and b != c:
        print("Yes")
    elif c == d and c == e and c != a and c != b:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()