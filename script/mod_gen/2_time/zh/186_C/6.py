def main():
    n = int(input())
    result = 0
    for i in range(1, n+1):
        if '7' not in str(i) and '7' not in oct(i):
            result += 1
    print(result)

if __name__ == '__main__':
    main()