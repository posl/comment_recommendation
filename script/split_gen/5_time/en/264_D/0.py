def main():
    s = input()
    t = "atcoder"
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    print(count)
