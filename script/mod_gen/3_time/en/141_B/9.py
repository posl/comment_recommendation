def main():
    s = input()
    if (len(s) % 2 == 0):
        if (s[1::2] == "RUD" * (len(s) // 2)):
            print("Yes")
        else:
            print("No")
    else:
        if (s[0::2] == "RUD" * (len(s) // 2) + "R"):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()