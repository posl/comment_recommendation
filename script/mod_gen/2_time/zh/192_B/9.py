def isDifficult():
    s = input()
    if s == s.lower():
        print("Yes")
    elif s == s.upper():
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    isDifficult()