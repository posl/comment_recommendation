def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] == i+1:
            ans += 1
    if ans == n:
        print(0)
    elif ans == n-1:
        print(1)
    elif ans == n-2:
        if a[0] == n and a[n-1] == 1:
            print(3)
        else:
            print(2)
    else:
        print(-1)
