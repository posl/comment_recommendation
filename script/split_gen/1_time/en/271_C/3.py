def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if a[i] <= i + 1:
            ans = i + 1
        else:
            break
    print(ans)
