def median(a):
    a.sort()
    n = len(a)
    if n%2 == 0:
        return (a[n//2-1]+a[n//2])//2
    else:
        return a[n//2]
n = int(input())
a = list(map(int, input().split()))
m = []
for i in range(n):
    for j in range(i,n):
        m.append(median(a[i:j+1]))
print(median(m))

if __name__ == '__main__':
    median()