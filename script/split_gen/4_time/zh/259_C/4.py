def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    if n+1 != m:
        print("No")
        return
    i = 0
    j = 0
    while i < n and j < m:
        if s[i] == t[j]:
            i += 1
            j += 1
            continue
        if s[i] != t[j] and s[i] == t[j+1]:
            j += 2
            continue
        print("No")
        return
    print("Yes")
