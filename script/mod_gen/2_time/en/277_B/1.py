def main():
    n = int(input())
    s = [input() for i in range(n)]
    if len(set(s)) != n:
        print("No")
        return
    for i in range(n):
        if s[i][0] not in "HDCS" or s[i][1] not in "A23456789TJQK":
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()