def main():
    n = int(input())
    s = set()
    for i in range(n):
        s.add(input())
    if len(s) == n and all(s[i][0] in "HDCS" and s[i][1] in "A23456789TJQK" for i in range(n)):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()