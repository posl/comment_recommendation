def problem175_b():
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    count = 0
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if l[i] != l[j] and l[i] != l[k] and l[j] != l[k]:
                    if l[i] + l[j] > l[k]:
                        count += 1
    print(count)
problem175_b()
