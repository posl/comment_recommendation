def main():
    n = int(input())
    count = 0
    for i in range(n+1):
        if '7' not in str(i) and '7' not in oct(i)[2:]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()