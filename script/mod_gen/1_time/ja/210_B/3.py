def main():
    n = int(input())
    s = input()
    for i in range(n):
        if s[i] == "0":
            if i % 2 == 0:
                print("Takahashi")
            else:
                print("Aoki")
            return

if __name__ == '__main__':
    main()