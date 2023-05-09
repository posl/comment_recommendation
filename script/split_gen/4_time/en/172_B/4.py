def main():
    s = input()
    t = input()
    if s == t:
        print(0)
        return
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    print(count)
