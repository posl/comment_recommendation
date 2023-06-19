def get_max_value(N,M,x,y,z):
    max_value = 0
    for i in range(0,N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                value = abs(x[i])+abs(x[j])+abs(x[k])+abs(y[i])+abs(y[j])+abs(y[k])+abs(z[i])+abs(z[j])+abs(z[k])
                if value > max_value:
                    max_value = value
    return max_value
N,M = map(int,input().split())
x = []
y = []
z = []
for i in range(0,N):
    x_i,y_i,z_i = map(int,input().split())
    x.append(x_i)
    y.append(y_i)
    z.append(z_i)
print(get_max_value(N,M,x,y,z))
