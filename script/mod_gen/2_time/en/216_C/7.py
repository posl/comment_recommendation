def main():
    N = int(input())
    result = ""
    while N > 0:
        if N % 2 == 0:
            result += "B"
            N //= 2
        else:
            result += "A"
            N -= 1
    print(result[::-1])

if __name__ == '__main__':
    main()