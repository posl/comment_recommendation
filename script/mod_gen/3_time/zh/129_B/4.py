def main():
    n = int(input())
    w = list(map(int, input().split()))
    result = 100
    for i in range(1, n):
        s1 = sum(w[:i])
        s2 = sum(w[i:])
        if result > abs(s1 - s2):
            result = abs(s1 - s2)
    print(result)

if __name__ == '__main__':
    main()