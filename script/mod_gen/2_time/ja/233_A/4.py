def main():
    x,y = map(int,input().split())
    if y % 10 == 0:
        if y <= x:
            print(0)
        else:
            print((y-x)//10)
    else:
        if y <= x:
            print(0)
        else:
            print((y-x)//10+1)

if __name__ == '__main__':
    main()