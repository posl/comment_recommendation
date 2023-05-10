def main():
    s = input()
    t = input()
    count = 0
    for i in range(0,len(s)):
        if s[i] != t[i]:
            count += 1
    print(count)
