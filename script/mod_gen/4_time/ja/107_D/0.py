def median(a):
    a.sort()
    if len(a) % 2 == 1:
        return a[len(a) // 2]
    else:
        return (a[len(a) // 2] + a[len(a) // 2 - 1]) // 2
N = int(input())
a = list(map(int, input().split()))
m = []
for i in range(N):
    for j in range(i, N):
        m.append(median(a[i:j + 1]))
print(median(m))

if __name__ == '__main__':
    median()