def main():
    n,x,y = map(int,input().split())
    u = [0] * (n-1)
    v = [0] * (n-1)
    for i in range(n-1):
        u[i],v[i] = map(int,input().split())
    for i in range(n-1):
        if u[i] == x and v[i] == y:
            print(x,y)
            break
        elif u[i] == y and v[i] == x:
            print(y,x)
            break
        elif u[i] == x:
            print(u[i],end=" ")
            x = v[i]
        elif v[i] == x:
            print(v[i],end=" ")
            x = u[i]
        elif u[i] == y:
            print(u[i],end=" ")
            y = v[i]
        elif v[i] == y:
            print(v[i],end=" ")
            y = u[i]
