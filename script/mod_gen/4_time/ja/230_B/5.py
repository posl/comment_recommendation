def main():
    s = input()
    t = s * 100000
    if s in t:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()