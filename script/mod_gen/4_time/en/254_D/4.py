def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i*j <= N and i == j:
                count += 1
            elif i*j <= N and i != j:
                count += 2
    print(count//2)

if __name__ == '__main__':
    main()