def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 1
    for i, p in enumerate(P):
        ans = max(ans, i+2-p)
    print(ans)
