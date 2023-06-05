def main():
    n = int(input())
    d = list(map(int, input().split()))
    print(sum([d[i] * d[j] for i in range(n) for j in range(i + 1, n)]))

if __name__ == '__main__':
    main()