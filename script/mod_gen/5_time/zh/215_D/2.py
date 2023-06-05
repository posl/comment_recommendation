def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
n,m=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
a.sort()
b=[]
for i in range(1,m+1):
    flag=0
    for j in a:
        if gcd(i,j)==1:
            flag=1
            break
    if flag==0:
        b.append(i)
print(len(b))
for i in b:
    print(i)

if __name__ == '__main__':
    gcd()