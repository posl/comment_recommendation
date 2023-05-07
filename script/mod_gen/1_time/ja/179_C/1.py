def main():
    N = int(input())
    count = 0
    for A in range(1, N):
        for B in range(1, N):
            C = N - (A * B)
            if C < 1:
                break
            count += 1
    print(count)

if __name__ == '__main__':
    main()