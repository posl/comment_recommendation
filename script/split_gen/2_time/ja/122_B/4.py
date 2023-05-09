def main():
    s = input()
    count = 0
    max_count = 0
    for i in range(len(s)):
        if s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or s[i] == 'T':
            count += 1
        else:
            count = 0
        if count > max_count:
            max_count = count
    print(max_count)
