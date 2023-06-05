def main():
    x,y,n = map(int,input().split())
    result = 0
    if n%3 == 0:
        result = (y//3)*n
    elif n%3 == 1:
        result = (y//3)*(n-1)+x
    elif n%3 == 2:
        result = (y//3)*(n-2)+x*2
    print(result)

if __name__ == '__main__':
    main()