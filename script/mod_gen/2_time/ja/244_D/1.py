def main():
    s = input()
    t = input()
    if s.count("R") % 2 == t.count("R") % 2 and s.count("G") % 2 == t.count("G") % 2 and s.count("B") % 2 == t.count("B") % 2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()