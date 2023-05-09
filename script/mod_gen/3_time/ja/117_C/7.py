def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    x.sort()
    if n >= m:
        print(0)
        exit()
    sub = []
    for i in range(m-1):
        sub.append(x[i+1]-x[i])
    sub.sort()
    print(sum(sub[:m-n]))

if __name__ == '__main__':
    main()