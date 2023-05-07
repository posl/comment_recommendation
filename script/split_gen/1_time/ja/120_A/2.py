def main():
    # input
    A, B, C = map(int, input().split())
    # compute
    ans = min(B//A, C)
    # output
    print(ans)
