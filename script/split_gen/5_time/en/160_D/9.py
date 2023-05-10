def main():
    n,x,y = map(int,input().split())
    #print(n,x,y)
    #print('Hello World!')
    dist = [0] * (n)
    for i in range(1,n):
        for j in range(i+1,n+1):
            dist[min(abs(i-j),abs(x-i)+1+abs(y-j),abs(y-i)+1+abs(x-j))] += 1
    for i in range(1,n):
        print(dist[i])
    return 0
