def main():
    s = input()
    t = input()
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    if i == len(s):
        print('Yes')
    else:
        print('No')
