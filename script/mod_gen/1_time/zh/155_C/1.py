def main():
    n = int(input())
    list = []
    for i in range(n):
        list.append(input())
    list.sort()
    d = {}
    for i in list:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    max = 0
    for i in d:
        if d[i] > max:
            max = d[i]
    for i in d:
        if d[i] == max:
            print(i)

if __name__ == '__main__':
    main()