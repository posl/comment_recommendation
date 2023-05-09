def main():
    N = int(input())
    count = 0
    #N円以上になる日を探す
    for i in range(1, N + 1):
        count += i
        if count >= N:
            print(i)
            break

if __name__ == '__main__':
    main()