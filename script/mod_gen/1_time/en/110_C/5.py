def main():
    s = input()
    t = input()
    if len(set(s)) < len(set(t)):
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()