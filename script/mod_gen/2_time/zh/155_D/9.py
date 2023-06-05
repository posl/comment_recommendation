def main():
    n = int(input())
    d = {}
    for i in range(n):
        s = input()
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    max = 0
    for s in d:
        if d[s] > max:
            max = d[s]
    for s in sorted(d):
        if d[s] == max:
            print(s)

if __name__ == '__main__':
    main()