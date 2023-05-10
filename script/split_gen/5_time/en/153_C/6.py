def main():
    N, K = [int(x) for x in input().split()]
    H = [int(x) for x in input().split()]
    H.sort()
    H.reverse()
    print(sum(H[K:]))
