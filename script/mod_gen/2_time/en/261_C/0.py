def main():
    n = int(input())
    d = {}
    for i in range(n):
        s = input()
        if s not in d:
            d[s] = 0
            print(s)
        else:
            d[s] += 1
            print(s + '(' + str(d[s]) + ')')
main()

if __name__ == '__main__':
    main()