def main():
    s = [input() for i in range(4)]
    if s.count("H") == 1 and s.count("2B") == 1 and s.count("3B") == 1 and s.count("HR") == 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()