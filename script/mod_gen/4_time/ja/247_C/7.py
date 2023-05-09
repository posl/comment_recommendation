def main():
    n = int(input())
    result = [1]
    for i in range(1,n):
        result = result + [i+1] + result
    print(*result)

if __name__ == '__main__':
    main()