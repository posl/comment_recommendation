def main():
    # input
    S = input()
    # compute
    ans = 0
    for i in range(4):
        if S[i] == '+':
            ans += 1
        else:
            ans -= 1
    # output
    print(ans)
