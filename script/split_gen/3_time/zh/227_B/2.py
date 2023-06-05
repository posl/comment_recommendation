def main():
    N = int(input())
    S = list(map(int, input().split()))
    ans = 0
    for s in S:
        if s % 2 == 0:
            ans += 1
        elif s % 3 == 0:
            ans += 1
        elif s % 5 == 0:
            ans += 1
    print(ans)
