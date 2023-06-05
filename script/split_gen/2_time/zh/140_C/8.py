def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    total = 0
    for i in range(n):
        total += b[a[i]-1]
        if i < n - 1 and a[i+1] - a[i] == 1:
            total += c[a[i]-1]
    print(total)
