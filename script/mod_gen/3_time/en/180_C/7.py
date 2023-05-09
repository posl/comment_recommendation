def main():
    N = int(input())
    result = []
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            result.append(i)
            if i != N // i:
                result.append(N // i)
    result.sort()
    for i in result:
        print(i)

if __name__ == '__main__':
    main()