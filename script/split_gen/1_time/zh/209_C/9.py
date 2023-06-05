def main():
    n = int(input())
    c = list(map(int,input().split()))
    c.sort()
    ans = 1
    for i in range(n):
        ans = ans * max(0,c[i]-i) % 1000000007
    print(ans)
