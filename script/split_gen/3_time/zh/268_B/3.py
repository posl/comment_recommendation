def main():
    s = input()
    t = input()
    if s in t[0:len(s)]:
        print("Yes")
    else:
        print("No")
