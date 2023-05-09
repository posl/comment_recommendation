def main():
    s = input()
    max_len = 0
    temp_len = 0
    for i in range(len(s)):
        if s[i] in 'ACGT':
            temp_len += 1
        else:
            temp_len = 0
        max_len = max(max_len, temp_len)
    print(max_len)
