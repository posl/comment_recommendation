def main():
    s = input()
    t = input()
    count = 0
    for i in range(len(s)):
        if s[i] == t[i]:
            count += 1
    if count == len(s):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()