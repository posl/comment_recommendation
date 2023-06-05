def main():
    s = input()
    max = 0
    count = 0
    for i in range(len(s)):
        if s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or s[i] == 'T':
            count += 1
        else:
            count = 0
        if count > max:
            max = count
    print(max)
