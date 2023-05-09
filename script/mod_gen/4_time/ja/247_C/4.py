def main():
    n = int(input())
    if n == 1:
        print(1)
    else:
        result = [1]
        for i in range(1, n):
            result = result + [i+1] + result
        print(*result)

if __name__ == '__main__':
    main()