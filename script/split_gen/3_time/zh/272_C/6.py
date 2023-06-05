def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    if a[0] % 2 == 1:
        print(-1)
    else:
        for i in range(1, n):
            if a[i] % 2 == 0:
                print(a[0])
                break
        else:
            print(-1)
