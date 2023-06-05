def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s = set(s)
    for i in s:
        if i[0] == '!':
            if i[1:] in s:
                print(i[1:])
                return
        elif '!' + i in s:
            print(i)
            return
    print('satisfiable')

if __name__ == '__main__':
    main()