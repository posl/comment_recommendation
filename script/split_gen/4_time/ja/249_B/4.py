def main():
    s = input()
    s = list(s)
    for i in range(len(s)):
        for j in range(len(s)):
            if i != j and s[i] == s[j]:
                print("No")
                return
    print("Yes")
    return
