def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(2**n):
        b.append(a[i])
    for i in range(n):
        for j in range(2**(n-i-1)):
            if b[2*j] > b[2*j+1]:
                b[j] = b[2*j]
            else:
                b[j] = b[2*j+1]
    for i in range(2**n):
        if a[i] == b[0]:
            print(i+1)
