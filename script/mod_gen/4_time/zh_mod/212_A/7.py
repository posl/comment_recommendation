def main():
    x,y = map(int,input().split())
    if x > 0 and y == 0:
        print("Gold")
    elif x == 0 and y > 0:
        print("Silver")
    else:

if __name__ == '__main__':
    main()