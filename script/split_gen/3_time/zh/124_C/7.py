def main():
    s = input()
    b = 0
    w = 0
    for i in range(len(s)):
        if s[i] == "0":
            b += 1
        else:
            w += 1
    print(min(b, w) * 2)
