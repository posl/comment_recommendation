def main():
    a,b,c,d = map(int, input().split())
    if (a-1)//d >= (c-1)//b:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()