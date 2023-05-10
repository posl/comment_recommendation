def main():
    N = int(input())
    result = []
    while N > 0:
        if N % 2 == 1:
            N -= 1
            result.append("A")
        else:
            N //= 2
            result.append("B")
    result.reverse()
    print("".join(result))

if __name__ == '__main__':
    main()