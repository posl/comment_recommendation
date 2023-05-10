def main():
    n,m,x,y = map(int,input().split())
    xlist = list(map(int,input().split()))
    ylist = list(map(int,input().split()))
    xlist.append(x)
    ylist.append(y)
    xlist.sort()
    ylist.sort()
    if xlist[-1] < ylist[0]:
        print("No War")
    else:
        print("War")

if __name__ == '__main__':
    main()