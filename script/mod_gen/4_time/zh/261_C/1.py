def main():
    n = int(input())
    d = {}
    for i in range(n):
        s = input()
        if s in d:
            d[s] += 1
            print(s + "(" + str(d[s]) + ")")
        else:
            d[s] = 0
            print(s)

if __name__ == '__main__':
    main()