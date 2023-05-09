def median(list):
    list.sort()
    if len(list) % 2 == 0:
        return (list[int(len(list)/2)-1] + list[int(len(list)/2)]) / 2
    else:
        return list[int(len(list)/2)]
N = int(input())
a = list(map(int, input().split()))
m = []
for i in range(N):
    for j in range(i, N):
        m.append(median(a[i:j+1]))
print(int(median(m)))

if __name__ == '__main__':
    median()