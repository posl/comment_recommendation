def main():
    n = int(input())
    s = [input() for i in range(n)]
    s = set(s)
    if len(s) == n:
        print('satisfiable')
    else:
        for i in s:
            if '!' + i in s:

if __name__ == '__main__':
    main()