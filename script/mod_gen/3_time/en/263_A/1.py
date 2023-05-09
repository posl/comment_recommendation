def main():
    a,b,c,d,e = map(int,input().split())
    if (a == b == c and d == e) or (a == b and c == d == e):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()