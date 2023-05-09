def main():
    N = int(input())
    s = input().rstrip()
    if s[N-1] == "o":
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()