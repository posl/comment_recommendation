def main():
    n = int(input())
    s = set()
    for i in range(n):
        s.add(input())
    if len(s) == n and all(x[0] in 'HDCS' and x[1] in 'A23456789TJQK' for x in s):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()