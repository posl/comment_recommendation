def main():
    # input
    K = int(input())
    S = input()
    # compute
    if len(S) <= K:
        ans = S
    else:
        ans = S[:K] + '...'
    # output
    print(ans)
