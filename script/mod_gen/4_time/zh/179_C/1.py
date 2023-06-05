def main():
    n = int(input())
    count = 0
    for a in range(1, n):
        for b in range(1, n):
            if a*b < n:
                count += 1
            else:
                break
    print(count)

if __name__ == '__main__':
    main()