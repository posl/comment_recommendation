def median(a):
    a.sort()
    return a[len(a)//2]
n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    for j in range(i, n):
        b.append(median(a[i:j+1]))
print(median(b))

if __name__ == '__main__':
    median()