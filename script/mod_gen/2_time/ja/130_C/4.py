def main():
    W,H,x,y = map(int,input().split())
    if W == x or H == y:
        print(0.5*W*H,0)
    else:
        print(0.5*W*H,1)

if __name__ == '__main__':
    main()