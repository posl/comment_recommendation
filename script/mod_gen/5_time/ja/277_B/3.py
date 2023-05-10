def main():
    n = int(input())
    s = [input() for i in range(n)]
    if len(s) == len(set(s)):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()