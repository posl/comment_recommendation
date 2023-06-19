def main():
    x,y,z = map(int,input().split())
    if (x*y*z) == 0:
        print(-1)
    elif x*y*z > 0:
        print(-1)
    else:
        print(abs(x-y)+abs(y-z)+abs(z-x))

if __name__ == '__main__':
    main()