def main():
    x,y,z = map(int,input().split())
    if x<z:
        print(-1)
    elif x<z+y:
        print(z+y-x)
    else:
        print(0)

if __name__ == '__main__':
    main()