def main():
    W,H,x,y=map(int,input().split())
    ans1=0
    ans2=0
    if x*2==W and y*2==H:
        ans1=W*H/2
        ans2=1
    else:
        ans1=W*H/2
        ans2=0
    print(ans1,ans2)

if __name__ == '__main__':
    main()