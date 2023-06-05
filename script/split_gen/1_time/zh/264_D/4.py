def main():
    s = input()
    t = "atcoder"
    count = 0
    for i in range(len(s)):
        if s[i] == t[i]:
            continue
        else:
            count += 1
    print(count)
