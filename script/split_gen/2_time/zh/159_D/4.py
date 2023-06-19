def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    c = [0] * (n+1)
    for x in a:
        c[x] += 1
    ans = 0
    for x in c:
        ans += x * (x-1) // 2
    for x in a:
        print(ans - c[x] + 1)
