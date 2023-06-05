def main():
    n = int(input())
    s = [input() for i in range(n)]
    # print(s)
    s = set(s)
    # print(s)
    for i in s:
        if '!' + i in s:
            print(i)
            return
    print('satisfiable')

if __name__ == '__main__':
    main()