def main():
    s = input()
    t = input()
    if len(s) == len(t):
        if t in (s + s):
            print("Yes")
        else:
            print("No")
    else:
        print("No")
