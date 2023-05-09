def main():
    n = int(input())
    s = [input() for _ in range(n)]
    for i in range(n):
        if '!' + s[i] in s:
            print(s[i])
            return
    print('satisfiable')

if __name__ == '__main__':
    main()