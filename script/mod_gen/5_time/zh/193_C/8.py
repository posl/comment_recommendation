def main():
    n = int(input())
    res = n
    for i in range(2, int(n**0.5)+1):
        j = 2
        while i**j <= n:
            res -= 1
            j += 1
    print(res)

if __name__ == '__main__':
    main()