def main():
    s = input()
    t = input()
    if sorted(s) != sorted(t):
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()