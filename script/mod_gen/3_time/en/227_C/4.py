def main():
    n = int(input())
    count = 0
    for a in range(1, n+1):
        for b in range(a, n+1):
            c = n // (a*b)
            if a <= b <= c:
                count += 1
    print(count)

if __name__ == '__main__':
    main()