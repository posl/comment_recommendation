def main():
    N, K = map(int, input().split())
    ans = N
    while True:
        if ans > abs(ans-K):
            ans = abs(ans-K)
        else:
            break
    print(ans)
