def main():
    n = int(input())
    ss = [input() for _ in range(n)]
    s1 = set()
    s2 = set()
    for s in ss:
        if s[0] == '!':
            s1.add(s[1:])
        else:
            s2.add(s)
    for s in s1:
        if s in s2:
            print(s)
            return
    print('satisfiable')

if __name__ == '__main__':
    main()