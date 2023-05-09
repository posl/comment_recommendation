def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if '7' in str(i) or '7' in oct(i)[2:]:
            continue
        count += 1
    print(count)
main()

if __name__ == '__main__':
    main()