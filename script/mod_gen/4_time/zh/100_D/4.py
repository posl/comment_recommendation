def myfun(x):
    return x[0]+x[1]+x[2]
n,m = input().split()
n = int(n)
m = int(m)
cake = []
for i in range(n):
    cake.append(list(map(int,input().split())))
cake.sort(key=myfun,reverse=True)
#print(cake)
max = 0
for i in range(m):
    max += abs(cake[i][0])
    max += abs(cake[i][1])
    max += abs(cake[i][2])
print(max)

if __name__ == '__main__':
    myfun()