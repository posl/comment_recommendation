def main():
    x,y = map(float,input().split("."))
    if y<=2:
        print(int(x),end="-")
    elif y<=6:
        print(int(x))
    else:
        print(int(x),end="+")

if __name__ == '__main__':
    main()