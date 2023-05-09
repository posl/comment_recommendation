def main():
    # input
    p, q, r = map(int, input().split())
    # compute
    # output
    print(min(p+q, q+r, r+p))
