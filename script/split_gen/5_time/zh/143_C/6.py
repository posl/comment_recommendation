def main():
    n = int(input())
    s = input()
    s = list(s)
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            s.pop(i)
        else:
            i += 1
    print(len(s))
