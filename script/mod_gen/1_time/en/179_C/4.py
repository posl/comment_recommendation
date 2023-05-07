def main():
    N = int(input())
    count = 0
    for A in range(1, N+1):
        for B in range(1, N+1):
            C = A*B - N
            if C < 1:
                continue
            if C % A == 0:
                count += 1
    print(count)

if __name__ == '__main__':
    main()