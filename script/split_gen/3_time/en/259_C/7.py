def main():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    if m < n:
        print("No")
        return
    for i in range(n):
        if s[n-i-1] != t[m-i-1]:
            print("No")
            return
    print("Yes")
    return
