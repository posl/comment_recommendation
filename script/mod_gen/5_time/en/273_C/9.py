def problems273_c():
    n = int(input())
    a = [int(i) for i in input().split()]
    # print(n)
    # print(a)
    a = sorted(a)
    # print(a)
    count = 1
    for i in range(1, n):
        if a[i-1] != a[i]:
            count += 1
    # print(count)
    for i in range(n):
        if a[i] == a[i-1]:
            print(count-1)
        else:
            print(count)
problems273_c()

if __name__ == '__main__':
    problems273_c()