def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    if s == t:
        print("Yes")
        return
    dic = {}
    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]] = t[i]
        else:
            if dic[s[i]] != t[i]:
                print("No")
                return
    print("Yes")
