def main():
    s = input()
    t = input()
    if len(s) + 1 == len(t):
        if s == t[:-1]:
            print("Yes")
            return
    print("No")
