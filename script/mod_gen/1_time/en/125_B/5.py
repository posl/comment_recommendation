def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    result = 0
    for i in range(n):
        if v[i] > c[i]:
            result += v[i] - c[i]
    print(result)

if __name__ == '__main__':
    main()