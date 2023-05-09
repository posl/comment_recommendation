def main():
    s = input()
    s1 = set(s)
    if len(s1) == 3:
        print(s[0])
    elif len(s1) == 2:
        print(list(s1 - set(s[0]))[0])
    else:
        print(-1)
