def main():
    s = input()
    t = input()
    n = len(s)
    for i in range(26):
        ans = True
        for j in range(n):
            if s[j] != t[(j+i)%n]:
                ans = False
                break
        if ans:
            print("Yes")
            return
    print("No")
