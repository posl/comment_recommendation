def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s = list(set(s))
    s.sort()
    s = [i[1:] for i in s if i[0] == '!']
    for i in s:
        if i in s:
            print(i)
            exit()
    print('satisfiable')

if __name__ == '__main__':
    main()