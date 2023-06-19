def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = a[:]
    b.sort()
    second = b[-2]
    print(a.index(second) + 1)
