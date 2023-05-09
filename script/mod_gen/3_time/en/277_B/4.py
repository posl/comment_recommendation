def main():
    n = int(input())
    s = set()
    for i in range(n):
        s.add(input())
    if len(s) != n:
        print('No')
        return
    for i in s:
        if i[0] not in 'HDCS' or i[1] not in 'A23456789TJQK':
            print('No')
            return
    print('Yes')
main()

if __name__ == '__main__':
    main()