def main():
    s = input()
    ans = 0
    count = 0
    for i in range(len(s)):
        if s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or s[i] == 'T':
            count += 1
            if count > ans:
                ans = count
        else:
            count = 0
    print(ans)
