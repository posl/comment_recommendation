def main():
    s = input()
    if len(s) == 1:
        print(0)
    else:
        count = 0
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                count += 1
        print(count)
