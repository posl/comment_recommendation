def main():
    a,b,c,d = map(int,input().split())
    if (a-1)//d >= c//b:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()