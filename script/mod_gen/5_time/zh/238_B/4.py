def pizza_cut(n,a):
    #n = int(input())
    #a = list(map(int,input().split()))
    a.sort()
    a.append(a[0]+360)
    #print(a)
    max_angle = 0
    for i in range(n):
        if max_angle < (a[i+1]-a[i]):
            max_angle = a[i+1]-a[i]
    return 360-max_angle

if __name__ == '__main__':
    pizza_cut()