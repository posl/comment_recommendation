def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if all(H[i] > H[j] for j in range(i)):
            count += 1
    print(count)

if __name__ == '__main__':
    main()