def main():
    N = int(input())
    count = 0
    for a in range(1, N):
        for b in range(1, N):
            c = N - a*b
            if c > 0:
                count += 1
    print(count)

if __name__ == '__main__':
    main()