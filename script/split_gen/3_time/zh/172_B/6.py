def main():
    s = input()
    t = input()
    # print(s)
    # print(t)
    # print(len(s))
    # print(len(t))
    # print(s[0])
    # print(t[0])
    # print(s[0] != t[0])
    # print(s[0] == t[0])
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    print(count)
