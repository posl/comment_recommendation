def main():
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    if s[0] + s[1] + s[2] == s[3] + s[4] and s[0] + s[4] == s[1] + s[3] and s[0] + s[3] == s[1] + s[2]:
        print(1)
    elif s[0] + s[1] + s[2] == s[3] + s[4]:
        print(2)
    elif s[0] + s[4] == s[1] + s[3] or s[0] + s[3] == s[1] + s[2]:
        print(2)
    elif s[0] + s[1] == s[2] + s[3] or s[0] + s[1] == s[2] + s[4] or s[0] + s[1] == s[3] + s[4] or s[0] + s[2] == s[1] + s[3] or s[0] + s[2] == s[1] + s[4] or s[0] + s[2] == s[3] + s[4]:
        print(2)
    elif s[0] + s[1] == s[2] + s[3] + s[4] or s[0] + s[2] == s[1] + s[3] + s[4]:
        print(2)
    elif s[0] + s[1] + s[2] == s[3] or s[0] + s[1] + s[2] == s[4]:
        print(2)
    else:
        print(3)
