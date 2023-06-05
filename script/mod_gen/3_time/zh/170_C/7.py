def main():
    x,n = map(int,input().split())
    p = list(map(int,input().split()))
    if n == 0:
        print(x)
        return
    else:
        for i in range(0,101):
            if i not in p:
                if abs(x-i) < abs(x-p[0]):
                    print(i)
                    return
                elif abs(x-i) == abs(x-p[0]) and i < p[0]:
                    print(i)
                    return
        print(p[0])
        return

if __name__ == '__main__':
    main()