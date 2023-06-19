def main():
    s = input()
    len_s = len(s)
    max_len = 0
    for i in range(len_s):
        for j in range(i, len_s):
            if all(c in 'ATCG' for c in s[i:j+1]):
                max_len = max(max_len, j - i + 1)
    print(max_len)
main()
