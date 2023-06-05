def main():
    n,m,x,y = map(int,input().split())
    xs = list(map(int,input().split()))
    ys = list(map(int,input().split()))
    xs.append(x)
    ys.append(y)
    xs.sort()
    ys.sort()
    if xs[-1] < ys[0]:
        print("No War")
    else:
        print("War")

if __name__ == '__main__':
    main()