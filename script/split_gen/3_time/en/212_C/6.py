def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 10**9
    for a in A:
        for b in B:
            ans = min(ans, abs(a-b))
    print(ans)
