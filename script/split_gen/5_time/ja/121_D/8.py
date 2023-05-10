def main():
    # input
    A, B = map(int, input().split())
    # compute
    ans = 0
    for i in range(A, B+1):
        ans ^= i
    # output
    print(ans)
