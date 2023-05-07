def main():
    N = int(input())
    count = 0
    for a in range(1, int(N ** (1/3)) + 1):
        for b in range(a, int((N / a) ** (1/2)) + 1):
            if N % (a * b) == 0:
                count += 1
                if a != b:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()