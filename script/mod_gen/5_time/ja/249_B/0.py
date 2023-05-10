def main():
    s = input()
    if s.islower() == False and s.isupper() == False and len(s) == len(set(s)):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()