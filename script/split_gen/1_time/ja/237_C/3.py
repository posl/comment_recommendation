def main():
    s = input()
    n = len(s)
    for i in range(n):
        if s[i] != s[n - i - 1]:
            print("No")
            exit()
    for i in range(n):
        if s[i] != s[n - i - 1 - i]:
            print("No")
            exit()
    print("Yes")
