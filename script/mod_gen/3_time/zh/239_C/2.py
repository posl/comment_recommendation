def main():
    x1,y1,x2,y2 = map(int, input().split())
    if (x1,y1) == (x2,y2):
        print("No")
        return
    elif abs(x1-x2) == abs(y1-y2):
        print("Yes")
        return
    else:
        print("No")
        return

if __name__ == '__main__':
    main()