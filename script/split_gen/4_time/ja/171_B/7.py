def main():
    # input
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    # compute
    print(sum(p[:k]))
    # output
