def main():
    a = [int(x) for x in input().split()]
    n = 0
    for i in range(10):
        n = a[n]
    print(n)
