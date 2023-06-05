def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort()
    sum = 0
    for i in range(n):
        if i == n-1:
            sum += p[i]/2
        else:
            sum += p[i]
    print(int(sum))

if __name__ == '__main__':
    main()