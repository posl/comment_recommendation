def main():
    s = input()
    t = input()
    i = 0
    while i < len(s):
        if s[i] != t[i]:
            break
        i += 1
    print(i+1)
