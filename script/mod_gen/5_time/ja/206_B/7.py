def main():
    N = int(input())
    total = 0
    for i in range(1, N + 1):
        total += i
        if total >= N:
            print(i)
            break

if __name__ == '__main__':
    main()