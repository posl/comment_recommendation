def problem122_b(s):
    max_len = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if isACGT(s[i:j]):
                max_len = max(max_len,j-i)
    return max_len

if __name__ == '__main__':
    problem122_b()