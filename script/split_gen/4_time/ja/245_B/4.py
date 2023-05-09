def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] != 0:
        print(0)
    else:
        for i in range(1,n):
            if a[i] - a[i-1] > 1:
                print(a[i-1]+1)
                break
        else:
            print(a[-1]+1)
