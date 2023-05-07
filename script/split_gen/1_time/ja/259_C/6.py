def main():
    s = input()
    t = input()
    #print(s,t)
    if len(s) > len(t):
        print("No")
        return
    for i in range(len(t)-len(s)+1):
        #print(i)
        count = 0
        for j in range(len(s)):
            if s[j] == t[i+j] or t[i+j] == "?":
                count += 1
            else:
                break
        if count == len(s):
            print("Yes")
            return
    print("No")
