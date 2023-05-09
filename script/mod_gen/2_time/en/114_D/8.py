def main():
    N = int(input())
    a = [0] * 100001
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            k = i
            while k % j == 0:
                a[j] += 1
                k //= j
    print(sum([1 for i in range(1, 100001) if a[i] == 75]))

if __name__ == '__main__':
    main()