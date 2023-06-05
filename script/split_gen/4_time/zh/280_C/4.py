def main():
    s = input()
    t = input()
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i = i + 1
        j = j + 1
    print(j)
