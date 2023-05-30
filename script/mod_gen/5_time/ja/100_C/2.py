def cal(a):
    count = 0
    for i in range(len(a)):
        while a[i]%2 == 0:
            a[i] = a[i] / 2
            count += 1
    return count
n = int(input())
a = list(map(int, input().split()))
print(cal(a))
