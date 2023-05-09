def main():
    N = int(input())
    H = list(map(int, input().split()))
    count = 1
    for i in range(1, N):
        if all([H[j] <= H[i] for j in range(i)]):
            count += 1
    print(count)

if __name__ == '__main__':
    main()