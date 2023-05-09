def main():
    # input
    N = int(input())
    S = input()
    # compute
    if S.count('1') % 2 == 0:
        ans = 'Takahashi'
    else:
        ans = 'Aoki'
    # output
    print(ans)
