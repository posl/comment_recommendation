def main():
    n,d = map(int,input().split())
    cnt = 0
    for i in range(n):
        x,y = map(int,input().split())
        if d**2 >= x**2 + y**2:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()