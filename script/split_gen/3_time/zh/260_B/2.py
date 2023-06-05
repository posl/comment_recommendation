def main():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(zip(a,b))
    c.sort(key=lambda x: x[0],reverse=True)
    c = c[:x]
    c.sort(key=lambda x: x[1],reverse=True)
    c = c[:x+y]
    c.sort(key=lambda x: x[0]+x[1],reverse=True)
    c = c[:x+y+z]
    c.sort(key=lambda x: x[0])
    for i in range(len(c)):
        print(c[i][0]+1)
