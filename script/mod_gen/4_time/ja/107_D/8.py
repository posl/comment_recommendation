def median(a):
    a.sort()
    return a[len(a)//2]
n = int(input())
a = list(map(int, input().split()))
m = []
for i in range(1, n+1):
    for j in range(i, n+1):
        m.append(median(a[i-1:j]))
print(median(m))

if __name__ == '__main__':
    median()