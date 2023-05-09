def check(s):
    for i in range(3):
        if s[i] == s[i+1]:
            return "Bad"
    return "Good"
s = input()
print(check(s))

if __name__ == '__main__':
    check()