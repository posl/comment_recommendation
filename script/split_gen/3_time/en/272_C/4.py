def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[-1] % 2 == 0:
        print(a[-1])
    elif a[-1] % 2 == 1:
        for i in range(n-1):
            if a[i] % 2 == 1:
                print(a[i] + a[i+1])
                break
        else:
            print(-1)
