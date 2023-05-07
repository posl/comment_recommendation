def main():
    s = input()
    if s[0] in "01" and s[1] in "0123" and s[2] in "01" and s[3] in "0123":
        print("AMBIGUOUS")
    elif s[0] in "01" and s[1] in "0123" and s[2] in "0123" and s[3] in "0123":
        print("MMYY")
    elif s[0] in "0123" and s[1] in "0123" and s[2] in "01" and s[3] in "0123":
        print("YYMM")
    else:
        print("NA")

if __name__ == '__main__':
    main()