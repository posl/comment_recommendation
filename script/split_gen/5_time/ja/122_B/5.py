def main():
    # input
    S = input()
    # compute
    max_len = 0
    for i in range(len(S)):
        for j in range(i, len(S)):
            if is_ATGC(S[i:j+1]):
                max_len = max(max_len, j-i+1)
    # output
    print(max_len)
