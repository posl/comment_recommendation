def main():
    s = input()
    max_len = 0
    count = 0
    for i in range(len(s)):
        if s[i] in 'ACGT':
            count += 1
            max_len = max(max_len, count)
        else:
            count = 0
    print(max_len)
