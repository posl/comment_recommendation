def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    print(s[-1])

if __name__ == '__main__':
    main()