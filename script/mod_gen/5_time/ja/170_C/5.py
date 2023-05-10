def main():
    x,n = map(int,input().split())
    if n == 0:
        print(x)
        return
    p = list(map(int,input().split()))
    if x not in p:
        print(x)
        return
    p.sort()
    for i in range(1,101):
        if x-i not in p:
            print(x-i)
            return
        elif x+i not in p:
            print(x+i)
            return

if __name__ == '__main__':
    main()