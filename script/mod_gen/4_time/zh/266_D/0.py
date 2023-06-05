def main():
    n = int(input())
    t = []
    x = []
    a = []
    for i in range(n):
        t_x_a = list(map(int, input().split()))
        t.append(t_x_a[0])
        x.append(t_x_a[1])
        a.append(t_x_a[2])
    #print(t)
    #print(x)
    #print(a)
    #print(t[0])
    #print(x[0])
    #print(a[0])
    sum = 0
    for i in range(n):
        if i == 0:
            if t[i] >= x[i]:
                sum += a[i]
        else:
            if t[i] - t[i-1] >= abs(x[i] - x[i-1]):
                sum += a[i]
    print(sum)

if __name__ == '__main__':
    main()