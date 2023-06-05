def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort()
    p.reverse()
    p[0] = p[0] / 2
    print(int(sum(p)))

if __name__ == '__main__':
    main()