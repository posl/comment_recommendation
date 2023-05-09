def main():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = []
    for i in range(n):
        c.append((a[i],b[i],i+1))
    c.sort(key=lambda x: x[2])
    c.sort(key=lambda x: x[1],reverse=True)
    c.sort(key=lambda x: x[0],reverse=True)
    d = c[:x+y+z]
    d.sort(key=lambda x: x[2])
    d.sort(key=lambda x: x[1],reverse=True)
    d.sort(key=lambda x: x[0],reverse=True)
    for i in range(x+y+z):
        print(d[i][2])
