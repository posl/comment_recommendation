def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    min = 100000
    index = 0
    for i in range(N):
        if abs(A - (T - H[i] * 0.006)) < min:
            min = abs(A - (T - H[i] * 0.006))
            index = i + 1
    print(index)

if __name__ == '__main__':
    main()