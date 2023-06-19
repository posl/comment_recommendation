def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    count = 0
    for i in range(n):
        if i == 0 or a[i] != a[i-1]:
            count = 1
        else:
            count += 1
        print(n - count)
