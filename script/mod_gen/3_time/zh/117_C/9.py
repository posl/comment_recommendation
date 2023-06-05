def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    x.sort()
    if n >= m:
        print(0)
        return
    distance = []
    for i in range(m-1):
        distance.append(x[i+1]-x[i])
    distance.sort()
    print(sum(distance[:m-n]))

if __name__ == '__main__':
    main()