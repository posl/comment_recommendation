def main():
    N = int(input())
    D = [0] * (10**9 + 2)
    for _ in range(N):
        A, B = map(int, input().split())
        D[A] += 1
        D[A+B] -= 1
    for i in range(1, 10**9 + 1):
        D[i] += D[i-1]
    print(*D[1:10**9+1])

if __name__ == '__main__':
    main()