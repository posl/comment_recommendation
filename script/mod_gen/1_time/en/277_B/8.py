def main():
    n = int(input())
    s = [input() for _ in range(n)]
    if len(set(s)) != n:
        print("No")
        return
    if not all(s[i][0] in "HDCS" for i in range(n)):
        print("No")
        return
    if not all(s[i][1] in "A23456789TJQK" for i in range(n)):
        print("No")
        return
    print("Yes")

if __name__ == '__main__':
    main()