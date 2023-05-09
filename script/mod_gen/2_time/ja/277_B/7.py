def main():
    n = int(input())
    s = [input() for _ in range(n)]
    if len(set(s)) == n and all(st in "HDCS" for st in [s[i][0] for i in range(n)]) and all(st in "A23456789TJQK" for st in [s[i][1] for i in range(n)]):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()