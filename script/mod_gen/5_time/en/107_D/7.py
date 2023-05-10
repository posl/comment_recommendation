def median(a):
    a.sort()
    if len(a)%2 == 0:
        return a[len(a)//2]
    else:
        return a[len(a)//2]
N = int(input())
a = list(map(int, input().split()))
b = []
for i in range(N):
    for j in range(i+1,N+1):
        b.append(median(a[i:j]))
print(median(b))

if __name__ == '__main__':
    median()