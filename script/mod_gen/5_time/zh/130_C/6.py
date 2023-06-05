def main():
    # W,H,x,y = map(int, input().split())
    # if x==0 or y==0 or x==W or y==H:
    #     print(W*H/2, 1)
    # else:
    #     print(W*H/2, 0)
    W,H,x,y = map(int, input().split())
    if x==0 or y==0 or x==W or y==H:
        print(W*H/2, 1)
    else:
        print(W*H/2, 0)

if __name__ == '__main__':
    main()