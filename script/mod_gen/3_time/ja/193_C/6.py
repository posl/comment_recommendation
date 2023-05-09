def main():
    N = int(input())
    a = [1] * (N+1)
    for i in range(2, N+1):
        for j in range(i, N+1, i):
            a[j] += 1
    print(sum(a) - 1 - N)

if __name__ == '__main__':
    main()