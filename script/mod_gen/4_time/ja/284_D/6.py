def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        for j in range(2, int(N**0.5)+1):
            if N % j == 0:
                if N % (j*j) == 0:
                    print(j, int(N/j/j))
                    break

if __name__ == '__main__':
    main()