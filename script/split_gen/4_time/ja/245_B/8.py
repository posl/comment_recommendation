def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    if a[0] != 0:
        print(0)
        return
    if n == 1:
        if a[0] == 0:
            print(1)
        else:
            print(0)
        return
    for i in range(1,n):
        if a[i] - a[i-1] > 1:
            print(a[i-1]+1)
            return
    print(a[-1]+1)
