def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    ans = 0
    if K > 0:
        ans = sum(H[:-K])
    else:
        ans = sum(H)
    print(ans)
