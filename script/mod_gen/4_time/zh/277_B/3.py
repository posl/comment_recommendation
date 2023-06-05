def main():
    n = int(input())
    s = [input() for i in range(n)]
    print("Yes" if len(s) == len(set(s)) and all([i[0] in "HDCS" and i[1] in "A23456789TJQK" for i in s]) else "No")

if __name__ == '__main__':
    main()