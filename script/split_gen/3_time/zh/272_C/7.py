def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    if a[0] == 0:
        a.pop(0)
    for i in range(len(a)-1, 0, -1):
        if a[i] == a[i-1]:
            a.pop(i)
    a.sort()
    #print(a)
    for i in range(len(a)-1, 0, -1):
        if a[i] % 2 == 0:
            print(a[i])
            return
        else:
            for j in range(i-1, -1, -1):
                if (a[i] + a[j]) % 2 == 0:
                    print(a[i]+a[j])
                    return
    print(-1)
    return
