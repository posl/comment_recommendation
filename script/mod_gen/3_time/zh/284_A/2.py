def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n-1, -1, -1):
        print(s[i])

if __name__ == '__main__':
    main()