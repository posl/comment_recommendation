def main():
    n = int(input())
    a = [input() for i in range(n)]
    if a.count("For") > a.count("Against"):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()