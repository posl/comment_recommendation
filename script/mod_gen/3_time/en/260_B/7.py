def main():
    #n: number of examinees
    #x: number of examinees with the highest math scores admitted
    #y: number of examinees with the highest English scores admitted
    #z: number of examinees with the highest total scores admitted
    #a: math scores
    #b: English scores
    #t: total scores
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    t = [a[i]+b[i] for i in range(n)]
    #sort by math score
    d = sorted([(a[i],b[i],t[i],i+1) for i in range(n)],reverse=True)
    #admit x examinees with the highest math scores
    for i in range(x):
        print(d[i][3])
    #sort by English score
    d = sorted([(a[i],b[i],t[i],i+1) for i in range(n) if i not in range(x)],reverse=True)
    #admit y examinees with the highest English scores
    for i in range(y):
        print(d[i][3])
    #sort by total score
    d = sorted([(a[i],b[i],t[i],i+1) for i in range(n) if i not in range(x+y)],reverse=True)
    #admit z examinees with the highest total scores
    for i in range(z):
        print(d[i][3])

if __name__ == '__main__':
    main()