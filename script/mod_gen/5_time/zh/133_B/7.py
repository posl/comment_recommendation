def distance(x,y):
    sum=0
    for i in range(len(x)):
        sum+=pow((x[i]-y[i]),2)
    return pow(sum,0.5)
n,d=map(int,input().split())
x=[]
for i in range(n):
    x.append(list(map(int,input().split())))
count=0
for i in range(n):
    for j in range(i+1,n):
        if distance(x[i],x[j]).is_integer():
            count+=1
print(count)

if __name__ == '__main__':
    distance()