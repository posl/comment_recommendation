def main():
    N = int(input())
    A = map(int, input().split())
    ans = 360
    for a in A:
        ans = min(ans, 360 - a)
    print(ans)
