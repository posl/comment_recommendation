def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    count = 0
    for i in range(n):
        a = list(map(int, input().split()))
        if sum([ai*bi for ai, bi in zip(a, b)]) + c > 0:
            count += 1
    print(count)

if __name__ == '__main__':
    main()