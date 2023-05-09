def main():
    N = int(input())
    D = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(i, N + 1, i):
            D[j] += 1
    print(D.count(75))
main()

if __name__ == '__main__':
    main()