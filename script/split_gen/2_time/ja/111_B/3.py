def check(n):
    s = str(n)
    if s[0] == s[1] and s[1] == s[2]:
        return True
    return False
n = int(input())
while True:
    if check(n):
        print(n)
        exit()
    n += 1
