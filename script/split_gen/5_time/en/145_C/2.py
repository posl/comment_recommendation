def dist(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**(1/2)
N=int(input())
towns=[]
for i in range(N):
    towns.append(list(map(int,input().split())))
    
total=0
for i in range(N):
    for j in range(N):
        total+=dist(towns[i],towns[j])
        
print(total/math.factorial(N))
