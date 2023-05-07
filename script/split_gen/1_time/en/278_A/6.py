def main():
    # input
    N, K = map(int, input().split())
    As = list(map(int, input().split()))
    # compute
    for i in range(K):
        As.append(0)
        As.pop(0)
    # output
    print(' '.join(map(str, As)))
