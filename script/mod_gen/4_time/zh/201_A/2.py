def main():
    a,b,c = map(int,input().split())
    if (c-b) == (b-a):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()