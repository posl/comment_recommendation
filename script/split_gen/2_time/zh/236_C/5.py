def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n == 1:
        print(a[0])
    else:
        for i in range(0, 4*n, 4):
            if a[i] != a[i+1]:
                print(a[i])
                break
            if a[i+2] != a[i+3]:
                print(a[i+2])
                break
