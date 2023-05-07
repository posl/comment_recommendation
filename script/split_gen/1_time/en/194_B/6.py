def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        tmp1, tmp2 = map(int, input().split())
        a.append(tmp1)
        b.append(tmp2)
    a.sort()
    b.sort()
    if n % 2 == 0:
        print((a[n//2-1]+a[n//2]+b[n//2-1]+b[n//2])//2)
    else:
        print(max(a[n//2], b[n//2]))
