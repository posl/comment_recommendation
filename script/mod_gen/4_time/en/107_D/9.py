def median(l):
    l.sort()
    return l[len(l)//2]
n = int(input())
a = list(map(int,input().split()))
m = []
for i in range(n):
    for j in range(i,n):
        m.append(median(a[i:j+1]))
print(median(m))

if __name__ == '__main__':
    median()