def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    sum = 0
    for i in range(n):
        for j in range(i):
            sum += (a[i] - a[j])**2
    print(sum)
