def func1():
    n,k=map(int,input().split())
    d=[]
    for i in range(k):
        d.append(int(input()))
        a=list(map(int,input().split()))
    res=n
    for i in range(n):
        for j in range(k):
            if i+1 in a:
                res-=1
                break
    print(res)

if __name__ == '__main__':
    func1()