def main():
    s = input()
    t = input()
    # s = "abbaac"
    # t = "abbbbaaac"
    # s = "xyzz"
    # t = "xyyzz"
    if len(s) >= len(t):
        print("No")
    else:
        if s == t[:len(s)]:
            print("Yes")
        else:
            print("No")
