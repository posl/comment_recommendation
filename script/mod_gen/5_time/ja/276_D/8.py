def func(a):
    count = 0
    for i in range(len(a)):
        while a[i] % 2 == 0:
            count += 1
            a[i] = a[i] / 2
        while a[i] % 3 == 0:
            count += 1
            a[i] = a[i] / 3
    return count
n = int(input())
a = list(map(int, input().split()))
count = func(a)

if __name__ == '__main__':
    func()