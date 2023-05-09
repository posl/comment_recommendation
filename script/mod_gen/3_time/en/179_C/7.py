def main():
    N = int(input())
    result = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if (i*j + j) == N:
                result += 1
    print(result)

if __name__ == '__main__':
    main()