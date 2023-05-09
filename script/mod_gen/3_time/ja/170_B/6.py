def main():
    x,y = map(int,input().split())
    if x*4>=y and y%2==0 and x*2<=y:
        print("Yes")
    else:
        print("No")
main()

if __name__ == '__main__':
    main()