def main():
    s = input()
    print("Yes") if s.count("A") == 1 or s.count("B") == 1 else print("No")

if __name__ == '__main__':
    main()