def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    ans = 0
    for i in range(n):
        ans += a[i] * b[i]
    if ans == 0:
        print("Yes")
    else:
        print("No")
