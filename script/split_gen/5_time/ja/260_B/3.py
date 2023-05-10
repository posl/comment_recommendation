def main():
    n,x,y,z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        c.append([i+1,a[i],b[i],a[i]+b[i]])
    c.sort(key=lambda x:(-x[3],x[0]))
    for i in range(x):
        print(c[i][0])
    for i in range(x,x+y):
        print(c[i][0])
    for i in range(x+y,x+y+z):
        print(c[i][0])
