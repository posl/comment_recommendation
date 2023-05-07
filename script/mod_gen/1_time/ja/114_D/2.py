def main():
    N = int(input())
    d = {}
    for i in range(2,N+1):
        d[i] = 0
    for i in range(2,N+1):
        for j in range(2,i+1):
            if i % j == 0:
                d[j] += 1
    c = 0
    for i in d.values():
        if i >= 2:
            c += 1
    print(c)

if __name__ == '__main__':
    main()