def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for a in A:
        B[a] += 1
    for i in range(1, N + 1):
        if B[i] % 2 == 1:
            print(i)
            return

if __name__ == '__main__':
    main()