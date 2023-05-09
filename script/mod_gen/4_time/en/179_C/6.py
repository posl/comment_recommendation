def main():
    N = int(input())
    count = 0
    for i in range(1, N):
        if i*i > N:
            break
        if N % i == 0:
            count += 1
            if i*i != N:
                count += 1
    print(count)

if __name__ == '__main__':
    main()