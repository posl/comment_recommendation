def main():
    a,b=map(int,input().split())
    if abs(a-b)==1 or abs(a-b)==4:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()