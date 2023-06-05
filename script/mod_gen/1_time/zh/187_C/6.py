def main():
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input())
    s = set(s)
    for i in s:
        if '!' + i in s:
            print(i)
            break
    else:
        print('satisfiable')

if __name__ == '__main__':
    main()