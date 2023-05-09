def main():
    W,H,x,y=map(int,input().split())
    a = W*H/2
    if W/2 == x and H/2 == y:
        b = 1
    else:
        b = 0
    print(a,b)

if __name__ == '__main__':
    main()