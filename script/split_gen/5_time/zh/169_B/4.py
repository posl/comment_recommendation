def main():
    n = int(input())
    a = list(map(int, input().split()))
    if 0 in a:
        print(0)
        return
    res = 1
    for i in range(n):
        res *= a[i]
        if res > 10**18:
            print(-1)
            return
    print(res)
