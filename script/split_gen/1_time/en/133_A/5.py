def main():
    # read input
    N, A, B = map(int, input().split())
    # compute
    train = N * A
    taxi = B
    # output
    print(min(train, taxi))
