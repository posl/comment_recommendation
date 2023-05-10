def main():
    n = int(input())
    s = set()
    for i in range(n):
        s.add(input())
    if len(s) == n:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()