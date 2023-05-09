def main():
    x,y,z=map(int,input().split())
    if z>y:
        print(-1)
    else:
        print(x+y-z)

if __name__ == '__main__':
    main()