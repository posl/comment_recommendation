def check(s, t):
    for i in range(len(t)):
        if s[i] != '?' and s[i] != t[i]:
            return False
    return True
s = input()
t = input()
for i in range(len(s) - len(t) + 1):
    if check(s[i:i+len(t)], t):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    check()