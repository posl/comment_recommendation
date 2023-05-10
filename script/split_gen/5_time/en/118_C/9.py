def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    #print(a)
    for i in range(n-1):
        if a[i] > 1:
            a[i+1] = a[i+1] % a[i]
            if a[i+1] == 0:
                a[i+1] = a[i]
    print(a[-1])
