def median(mas):
    mas.sort()
    if len(mas) % 2 == 0:
        return (mas[int(len(mas)/2)] + mas[int(len(mas)/2) - 1]) / 2
    else:
        return mas[int(len(mas)/2)]
n, k = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
min_median = float('inf')
for i in range(n-k+1):
    for j in range(n-k+1):
        mas = []
        for p in range(k):
            for q in range(k):
                mas.append(a[i+p][j+q])
        min_median = min(min_median, median(mas))
print(int(min_median))

if __name__ == '__main__':
    median()