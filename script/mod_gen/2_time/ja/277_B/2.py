def main():
    N = int(input())
    S = [input() for _ in range(N)]
    if len(S) != len(set(S)):
        print("No")
        return
    for s in S:
        if not s[0] in "HDCK":
            print("No")
            return
        if not s[1] in "A23456789TJQK":
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()