def main():
    N = int(input())
    result = 0
    for i in range(1, int(N ** (1/3)) + 1):
        for j in range(i, int((N / i) ** (1/2)) + 1):
            if i == j:
                result += 1
            else:
                result += 3
    print(result)

if __name__ == '__main__':
    main()