def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans = max(ans, max(p[i:])-i)
    print(ans+1)
