def main():
    N = int(input())
    day = 0
    total = 0
    while total < N:
        day += 1
        total += day
    print(day)

if __name__ == '__main__':
    main()