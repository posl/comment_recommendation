def main():
    s = input()
    if s[0] in "01" and s[1] in "0123456789" and s[2] in "01" and s[3] in "0123456789":
        print("AMBIGUOUS")
    elif s[0] in "01" and s[1] in "0123456789" and s[2] in "0" and s[3] in "0123456789":
        print("YYMM")
    elif s[0] in "0" and s[1] in "0123456789" and s[2] in "01" and s[3] in "0123456789":
        print("MMYY")
    else:
        print("NA")
