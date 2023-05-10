def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] != 0:
        print(0)
        return
    if a[-1] == 0:
        print(1)
        return
    for i in range(n-1):
        if a[i+1] - a[i] > 1:
            print(a[i]+1)
            return
    print(a[-1]+1)
