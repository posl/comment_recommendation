def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    b = []
    for i in range(n):
        b.append(a[i]-i-1)
    b.sort()
    if n % 2 == 0:
        print(b[n//2]-b[n//2-1])
    else:
        print(b[n//2])
