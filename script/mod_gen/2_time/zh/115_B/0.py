def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort()
    print(sum(p[0:n-1]) + p[n-1] // 2)

if __name__ == '__main__':
    main()