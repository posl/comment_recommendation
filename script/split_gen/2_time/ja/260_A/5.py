def main():
    s = input()
    for i in range(0, len(s)):
        if s.count(s[i]) == 1:
            print(s[i])
            return
    print(-1)
