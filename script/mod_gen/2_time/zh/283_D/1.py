def main():
    S = input()
    S = int(S)
    count = 0
    while S > 0:
        if S % 100 == 0:
            S = S // 100
        else:
            S = S - S % 10
        count += 1
    print(count)

if __name__ == '__main__':
    main()