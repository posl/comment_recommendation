def main():
    # input
    S = input()
    # compute
    res = 0
    count = 0
    for i in range(len(S)):
        if S[i]=='A' or S[i]=='C' or S[i]=='G' or S[i]=='T':
            count += 1
        else:
            count = 0
        res = max(res, count)
    # output
    print(res)
