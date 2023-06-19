def main():
    n = int(input())
    a = list(map(int,input().split()))
    a = sorted(a)
    if a[0] == 0:
        print(-1)
    else:
        if a[0] % 2 == 0:
            print(a[0])
        else:
            print(-1)
