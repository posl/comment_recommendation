def isBingo(a,b,c):
    for i in range(3):
        if a[i][0]==a[i][1]==a[i][2]==1 or a[0][i]==a[1][i]==a[2][i]==1:
            return True
    if a[0][0]==a[1][1]==a[2][2]==1 or a[0][2]==a[1][1]==a[2][0]==1:
        return True
    return False
a=[]
for i in range(3):
    a.append([0]*3)
for i in range(3):
    a[i]=list(map(int,input().split()))
n=int(input())
b=[]
for i in range(n):
    b.append(int(input()))
for i in range(n):
    for j in range(3):
        for k in range(3):
            if a[j][k]==b[i]:
                a[j][k]=1
                break

if __name__ == '__main__':
    isBingo()