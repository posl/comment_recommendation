def main():
    n,m,t=map(int,input().split())
    a=[int(x) for x in input().split()]
    xy=[]
    for i in range(m):
        xy.append([int(x) for x in input().split()])
    #print(n,m,t,a,xy)
    time=t
    room=1
    for i in range(n-1):
        time-=a[i]
        if time<=0:
            print('No')
            return
        if room==xy[0][0]:
            time+=xy[0][1]
            xy.pop(0)
        room+=1
    print('Yes')

if __name__ == '__main__':
    main()