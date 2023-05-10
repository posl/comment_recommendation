def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == '0':
            count += 1
    print(min(count, len(s) - count) * 2)
