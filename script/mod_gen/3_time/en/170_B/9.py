def main():
    x,y = map(int,input().split())
    
    if x >= 1 and x <= 100 and y >= 1 and y <= 100:
        if (y - 2*x) == 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()