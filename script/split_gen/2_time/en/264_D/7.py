def main():
    s = input()
    s = list(s)
    count = 0
    for i in range(7):
        if s[i] == 'a':
            continue
        elif s[i] == 't':
            continue
        elif s[i] == 'c':
            continue
        elif s[i] == 'o':
            continue
        elif s[i] == 'd':
            continue
        elif s[i] == 'e':
            continue
        elif s[i] == 'r':
            continue
        else:
            count += 1
    print(count)
