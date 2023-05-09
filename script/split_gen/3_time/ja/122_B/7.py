def main():
    s = input()
    str = ""
    count = 0
    for i in range(len(s)):
        if s[i] == "A" or s[i] == "C" or s[i] == "G" or s[i] == "T":
            str += s[i]
            count = max(count, len(str))
        else:
            str = ""
    print(count)
