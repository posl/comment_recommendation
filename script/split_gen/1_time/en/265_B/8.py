def main():
    #Get input
    n,m,t = map(int,input().split())
    a = list(map(int,input().split()))
    x = []
    y = []
    for i in range(m):
        x_i,y_i = map(int,input().split())
        x.append(x_i)
        y.append(y_i)
    
    #Initialize
    time = t
    room = 1
    
    #Move
    for i in range(n-1):
        time -= a[i]
        if time <= 0:
            print('No')
            return
        if (i+1) in x:
            time += y[x.index(i+1)]
        room += 1
    
    #Check if he can reach Room N
    if room == n:
        print('Yes')
    else:
        print('No')
    return
