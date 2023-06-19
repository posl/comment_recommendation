def main():
    n = int(input())
    A = list(map(int, input().split()))
    card = [0] * (n + 1)
    for i in range(4 * n - 1):
        card[A[i]] += 1
    for i in range(1, n + 1):
        if card[i] % 2 == 1:
            print(i)
            break

if __name__ == '__main__':
    main()