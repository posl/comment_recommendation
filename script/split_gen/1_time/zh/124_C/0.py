def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == '0' and i % 2 == 0:
            count += 1
        elif s[i] == '1' and i % 2 == 1:
            count += 1
    print(min(count, len(s) - count))
