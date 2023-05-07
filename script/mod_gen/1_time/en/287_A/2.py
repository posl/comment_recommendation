def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    f = s.count('For')
    a = s.count('Against')
    if f > a:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()