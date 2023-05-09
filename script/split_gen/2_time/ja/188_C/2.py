def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (2**n)
    for i in range(n):
        for j in range(2**(n-i-1)):
            if a[2*j] > a[2*j+1]:
                b[j] = a[2*j]
            else:
                b[j] = a[2*j+1]
        a = b
        b = [0] * (2**n)
    print(a.index(min(a))+1)
