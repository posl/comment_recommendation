def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        for j in range(2, int(n**0.5)+1):
            if n % j == 0:
                k = n // j
                if k % j == 0:
                    print(j, k // j)
                    break

if __name__ == '__main__':
    main()