def main():
    # input
    A, B, C = map(int, input().split())
    # compute
    ans = max(A+B, B+C, C+A)
    # output
    print(ans)
