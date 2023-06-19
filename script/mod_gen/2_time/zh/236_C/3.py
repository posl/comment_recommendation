def main():
    n, m = map(int, input().split())
    s = list(input().split())
    t = list(input().split())
    if n < m:
        print("No")
        return
    for i in range(n):
        if s[i] != t[i]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()