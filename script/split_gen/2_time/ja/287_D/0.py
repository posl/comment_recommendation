def main():
    s = input()
    t = input()
    for i in range(len(t)+1):
        if s[:i] + s[-(len(t)-i):] == t:
            print("Yes")
        else:
            print("No")
