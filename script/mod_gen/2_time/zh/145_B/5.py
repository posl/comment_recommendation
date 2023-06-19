def main():
    n = int(input())
    s = input()
    if n % 2 == 1:
        print("No")
        return
    for i in range(n//2):
        if s[i] != s[n//2+i]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()