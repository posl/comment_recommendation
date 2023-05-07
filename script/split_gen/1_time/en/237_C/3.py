def main():
    s = input()
    l = len(s)
    s1 = s[0:int((l-1)/2)]
    s2 = s[int((l+3)/2)-1:l]
    if s1 == s2:
        print("Yes")
    else:
        print("No")
