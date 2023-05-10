def main():
    s = input()
    t = input()
    for i in range(len(s)):
        for j in range(26):
            if s[i] == chr(ord("a") + j):
                s = s[:i] + chr(ord("a") + (j + 1) % 26) + s[i + 1:]
                break
    if s == t:
        print("Yes")
    else:
        print("No")
