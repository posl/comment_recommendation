def main():
    N = int(input())
    sum = 0
    for i in range(N):
        sum = sum + i + 1
        if sum >= N:
            break
    print(i+1)

if __name__ == '__main__':
    main()