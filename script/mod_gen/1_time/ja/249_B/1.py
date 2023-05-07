def main():
    s = input()
    if s.isupper() or s.islower():
        print("No")
    elif len(set(s)) == len(s):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()