def main():
    s = input()
    n = len(s)
    s1 = s[:int((n-1)/2)]
    s2 = s[int((n+3)/2)-1:]
    if s == s[::-1] and s1 == s1[::-1] and s2 == s2[::-1]:
        print("Yes")
    else:
        print("No")
