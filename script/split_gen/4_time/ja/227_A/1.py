def main():
    # input
    n, k, a = map(int, input().split())
    # compute
    # output
    if k % n == 0:
        print(n)
    else:
        print(k % n)
