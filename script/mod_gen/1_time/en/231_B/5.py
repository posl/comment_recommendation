def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    s.reverse()
    print(s[0])

if __name__ == '__main__':
    main()