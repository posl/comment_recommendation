def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i-1 for i in a]
    ans = 0
    b = [0]*n
    while b[x-1] == 0:
        b[x-1] = 1
        ans += 1
        x = a[x-1]+1
    print(ans)
