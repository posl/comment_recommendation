def main():
    s = input()
    t = input()
    if len(s) < len(t):
        print("No")
    else:
        if t in s:
            print("Yes")
        else:
            print("No")
