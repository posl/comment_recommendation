def main():
    s = input()
    t = ""
    max_len = 0
    for i in range(len(s)):
        if s[i] == "A" or s[i] == "C" or s[i] == "G" or s[i] == "T":
            t += s[i]
            max_len = max(max_len, len(t))
        else:
            t = ""
    print(max_len)
