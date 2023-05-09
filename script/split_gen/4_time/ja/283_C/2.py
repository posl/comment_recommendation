def main():
    # input
    S = input()
    # compute
    cnt = 0
    while len(S) > 1:
        if S[-1] == '0':
            S = S[:-1]
        else:
            S = str(int(S) - 1)
        cnt += 1
    # output
    print(cnt + int(S))
