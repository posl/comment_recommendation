def main():
    n = int(input())
    s = str(n)
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    if n % sum == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()