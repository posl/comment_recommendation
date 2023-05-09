def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s1 = [i[1:] for i in s if i[0] == '!']
    s2 = [i for i in s if i[0] != '!']
    for i in s1:
        if i in s2:
            print(i)
            return
    print('satisfiable')

if __name__ == '__main__':
    main()