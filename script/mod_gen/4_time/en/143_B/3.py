def main():
    n = int(input())
    d = list(map(int, input().split()))
    s = 0
    for i in range(n):
        for j in range(i+1, n):
            s += d[i]*d[j]
    print(s)

if __name__ == '__main__':
    main()