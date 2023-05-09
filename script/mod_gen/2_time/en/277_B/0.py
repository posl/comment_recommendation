def main():
    n = int(input())
    s = [input() for _ in range(n)]
    if len(set(s)) != n:
        print("No")
        return
    for i in range(n):
        if s[i][0] not in ["H", "D", "C", "S"]:
            print("No")
            return
        if s[i][1] not in ["A", "T", "J", "Q", "K"] and not s[i][1].isdecimal():
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()