def main():
    S = input()
    max_len = 0
    for i in range(len(S)):
        for j in range(i+1, len(S)+1):
            if is_acgt(S[i:j]):
                max_len = max(max_len, j-i)
    print(max_len)
