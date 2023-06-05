def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort()
    p.reverse()
    total = 0
    for i in range(n):
        if i == 0:
            total += p[i] / 2
        else:
            total += p[i]
    print(int(total))

if __name__ == '__main__':
    main()