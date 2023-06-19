def main():
    n = int(input())
    s = input()
    if len(s) % 2 == 0:
        if s[:int(len(s)/2)] == s[int(len(s)/2):]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()