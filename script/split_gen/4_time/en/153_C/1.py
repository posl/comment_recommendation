def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    if K == 0:
        print(sum(H))
    else:
        print(sum(H[K:]))
