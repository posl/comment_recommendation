def main():
    s = input()
    if "A" in s and "a" in s and len(set(s)) == len(s):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()