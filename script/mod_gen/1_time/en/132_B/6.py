def main():
    n = int(input())
    p = list(map(int, input().split()))
    print(sum([1 for i in range(1, n - 1) if p[i] > min(p[i - 1], p[i + 1]) and p[i] < max(p[i - 1], p[i + 1])]))

if __name__ == '__main__':
    main()