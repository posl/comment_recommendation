def calc(x,y):
    return int(((x-y)**2)**0.5)
n,m = map(int,input().split())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 and j == 1:
            print(0,end=" ")
        else:
            print(calc(1,i)+calc(1,j),end=" ")
    print()

if __name__ == '__main__':
    calc()