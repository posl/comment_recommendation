def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        print(s[n-i-1])

if __name__ == '__main__':
    main()