def main():
    N = int(input())
    count = 0
    for i in range(1, N + 1):
        if '7' in str(i) or '7' in str(oct(i))[2:]:
            continue
        else:
            count += 1
    print(count)

if __name__ == '__main__':
    main()