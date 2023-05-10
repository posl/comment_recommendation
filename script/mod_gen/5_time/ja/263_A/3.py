def main():
    a,b,c,d,e = map(int,input().split())
    if a==b and a==c and d==e:
        print("Yes")
    elif a==b and c==d and c==e:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()