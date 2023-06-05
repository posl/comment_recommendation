def problems241_a():
    a = [int(i) for i in input().split()]
    k = 0
    for i in range(3):
        k = a[k]
    print(k)

if __name__ == '__main__':
    problems241_a()