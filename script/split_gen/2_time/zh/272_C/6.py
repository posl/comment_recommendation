def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] % 2 == 0:
        print(a[0])
    elif a[1] % 2 == 0:
        print(a[1])
    elif a[0] + a[1] % 2 == 0:
        print(a[0] + a[1])
    else:
        print(-1)
