def main():
    S = input()
    max_len = 0
    len_S = len(S)
    for i in range(len_S):
        for j in range(i, len_S):
            if is_acgt(S[i:j+1]):
                max_len = max(max_len, j - i + 1)
    print(max_len)
