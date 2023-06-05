def check(a):
    n = len(a)
    # print(n)
    for i in range(n):
        if a[i] == 1:
            for j in range(n):
                if (j+1) % (i+1) == 0:
                    a[j] = (a[j] + 1) % 2
    if sum(a) == 0:
        return True
    else:
        return False
n = int(input())
a = list(map(int, input().split()))
