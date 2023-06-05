def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 0
    for i in range(n):
        if a[i] == i+1:
            ans += 1
    if ans == n:
        print(0)
    elif ans == n-1:
        print(1)
    else:
        print(n-ans)
