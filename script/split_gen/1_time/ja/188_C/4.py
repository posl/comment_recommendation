def main():
    n = int(input())
    a = list(map(int,input().split()))
    a = [0] + a
    for i in range(n):
        for j in range(1,2**(n-i),2):
            if a[j] > a[j+1]:
                a[j] = 0
            else:
                a[j+1] = 0
    print(a.index(0))
