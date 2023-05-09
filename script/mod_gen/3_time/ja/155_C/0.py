def main():
    n = int(input())
    d = {}
    for _ in range(n):
        s = input()
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    max = 0
    for k, v in d.items():
        if v > max:
            max = v
    l = []
    for k, v in d.items():
        if v == max:
            l.append(k)
    l.sort()
    for i in l:
        print(i)

if __name__ == '__main__':
    main()