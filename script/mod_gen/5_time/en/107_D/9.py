def median(a):
    a.sort()
    return a[len(a)//2]
n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    b.append(median(a[i:]))
print(median(b))

if __name__ == '__main__':
    median()