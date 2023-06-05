def main():
    a = [int(x) for x in input().split()]
    n = len(a)
    for i in range(1, n):
        a[i] = a[a[i]]
    print(a[3])
