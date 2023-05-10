def main():
    W,H,x,y = map(int,input().split())
    print(W*H/2, 1 if W*H/2==x*y else 0)

if __name__ == '__main__':
    main()