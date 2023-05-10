def f():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[n-1])
f()

if __name__ == '__main__':
    f()