def main():
    s = input()
    n = len(s)
    for i in range(n):
        if s[i] != s[n-1-i]:
            print("Yes")
            exit()
    print("No")
