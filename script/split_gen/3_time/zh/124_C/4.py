def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i] == '1':
            count += 1
        elif i % 2 == 1 and s[i] == '0':
            count += 1
    print(min(count, len(s) - count))
