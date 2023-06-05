def test():
    s = input()
    a = int(s[:2])
    b = int(s[2:])
    if a in range(1,13) and b in range(1,13):
        print("AMBIGUOUS")
    elif a in range(1,13) and b not in range(1,13):
        print("MMYY")
    elif a not in range(1,13) and b in range(1,13):
        print("YYMM")
    else:
        print("NA")
test()
