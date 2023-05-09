def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] != 0:
        print(0)
    else:
        for i in range(1,n):
            if a[i] - a[i-1] >= 2:
                print(a[i-1]+1)
                break
            elif i == n-1:
                print(a[n-1]+1)
