def main():
    n = int(input())
    d = {}
    for _ in range(n):
        s = input()
        if s not in d:
            d[s] = 0
        else:
            d[s] += 1
            s += '(' + str(d[s]) + ')'
        print(s)

if __name__ == '__main__':
    main()