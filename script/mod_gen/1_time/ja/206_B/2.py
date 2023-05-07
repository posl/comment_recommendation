def main():
    n = int(input())
    total = 0
    for i in range(1, 100000):
        total += i
        if total >= n:
            print(i)
            break

if __name__ == '__main__':
    main()