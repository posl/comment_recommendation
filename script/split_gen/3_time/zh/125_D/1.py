def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0
    cnt = 0
    for i in range(n):
        ans += abs(a[i])
        if a[i] < 0:
            cnt += 1
    if cnt % 2 == 0:
        print(ans)
    else:
        print(ans - 2 * min(abs(x) for x in a))
