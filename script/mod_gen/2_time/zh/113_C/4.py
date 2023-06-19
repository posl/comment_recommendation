def main():
    n,m = map(int,input().split())
    pm = []
    for i in range(m):
        p,y = map(int,input().split())
        pm.append([p,y])
    pm.sort(key=lambda x:x[1])
    print(pm)
    for i in range(m):
        print("{:06}{:06}".format(pm[i][0],i+1))

if __name__ == '__main__':
    main()