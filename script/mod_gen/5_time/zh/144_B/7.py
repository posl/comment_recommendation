def main():
    n = int(input())
    result = "No"
    for i in range(1,10):
        if n % i == 0 and n / i < 10:
            result = "Yes"
            break
    print(result)

if __name__ == '__main__':
    main()