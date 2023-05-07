def main():
    W,H,x,y=map(int,input().split())
    S = W*H/2
    if x==W/2 and y==H/2:
        print(S,1)
    else:
        print(S,0)

if __name__ == '__main__':
    main()