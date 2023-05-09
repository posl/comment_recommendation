def median(a):
    a = sorted(a)
    if len(a)%2 == 0:
        return (a[len(a)//2]+a[len(a)//2-1])/2
    else:
        return a[len(a)//2]
n = int(input())
a = list(map(int, input().split()))
m = []
for i in range(len(a)):
    for j in range(i, len(a)):
        m.append(median(a[i:j+1]))
print(median(m))

if __name__ == '__main__':
    median()