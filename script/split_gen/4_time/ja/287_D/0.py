def main():
    s = input()
    t = input()
    for i in range(len(s) - len(t) + 1):
        for j in range(len(t)):
            if s[i + j] != t[j] and s[i + j] != '?':
                break
        else:
            print('Yes')
            break
    else:
        print('No')
