def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    b[0] = 0
    for i in range(1, n):
        if a[i-1] < a[i]:
            b[i] = b[i-1] + 1
        else:
            b[i] = 0
    print(sum(b))

if __name__ == '__main__':
    main()