def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(input())
    l = sorted(l)
    max = 0
    for i in range(n):
        if l.count(l[i]) > max:
            max = l.count(l[i])
    for i in range(n):
        if l.count(l[i]) == max:
            print(l[i])

if __name__ == '__main__':
    main()