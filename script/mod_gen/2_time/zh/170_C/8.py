def main():
    x,n = map(int,input().split())
    if n == 0:
        print(x)
        exit()
    p = list(map(int,input().split()))
    num = 0
    for i in range(1,101):
        if i not in p:
            if abs(x-i) < abs(x-num):
                num = i
    print(num)

if __name__ == '__main__':
    main()