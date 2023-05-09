def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        st = input().split()
        s.append(st[0])
        t.append(st[1])
    if len(s) == len(set(s)) and len(t) == len(set(t)):
        print('Yes')
    else:
        print('No')
main()

if __name__ == '__main__':
    main()