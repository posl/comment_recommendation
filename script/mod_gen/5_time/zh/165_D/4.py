def main():
    a,b,n=map(int,input().split())
    max=0
    for x in range(0,n+1):
        if (a*x//b)-(a*(x//b))>max:
            max=(a*x//b)-(a*(x//b))
    print(max)
    return

if __name__ == '__main__':
    main()