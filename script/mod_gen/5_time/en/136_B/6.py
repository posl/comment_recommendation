def main():
    N = input()
    N = int(N)
    count = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 != 0:
            count += 1
    print(count)

if __name__ == '__main__':
    main()