def my_sort(x):
    return x[1]
n = int(input())
list = []
for i in range(n):
    a, b = map(int, input().split())
    list.append([a, b])
list.sort(key=my_sort)
time = 0
for i in range(n):
    time += list[i][0]
    if time > list[i][1]:
        print("No")
        exit()
print("Yes")

if __name__ == '__main__':
    my_sort()