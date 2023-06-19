def main():
    n = int(input())
    result = 0
    for i in range(1, n+1):
        temp = 0
        for j in range(i, n+1):
            temp += j
            if temp == n:
                result += 1
                break
            if temp > n:
                break
    print(result)

if __name__ == '__main__':
    main()